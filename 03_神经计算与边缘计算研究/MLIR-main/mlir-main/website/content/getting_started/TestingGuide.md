---
title: "Testing Guide"
date: 2019-11-29T15:26:15Z
draft: false
weight: 40
---

Testing is an integral part of any software infrastructure. In general, all
commits to the MLIR repository should include an accompanying test of some form.
Commits that include no functional changes, such as API changes like symbol
renaming, should be tagged with NFC(no functional changes). This signals to the
reviewer why the change doesn't/shouldn't include a test.

MLIR generally separates testing into three main categories, [Check](#check-tests)
tests, [Unit](#unit-tests) tests, and [Integration](#integration-tests) tests.

## Check tests

Check tests are tests that verify that some set of string tags appear in the
output of some program. These tests generally encompass anything related to the
state of the IR (and more); analysis, parsing, transformation, verification,
etc. They are written utilizing several different tools:

### FileCheck tests

[FileCheck](https://llvm.org/docs/CommandGuide/FileCheck.html) is a utility tool
that "reads two files (one from standard input, and one specified on the command
line) and uses one to verify the other." Essentially, one file contains a set of
tags that are expected to appear in the output file. MLIR utilizes FileCheck, in
combination with [lit](https://llvm.org/docs/CommandGuide/lit.html), to verify
different aspects of the IR - such as the output of a transformation pass.

An example FileCheck test is shown below:

```mlir
// RUN: mlir-opt %s -cse | FileCheck %s

// CHECK-LABEL: func.func @simple_constant
func.func @simple_constant() -> (i32, i32) {
  // CHECK-NEXT: %[[RESULT:.*]] = arith.constant 1
  // CHECK-NEXT: return %[[RESULT]], %[[RESULT]]

  %0 = arith.constant 1 : i32
  %1 = arith.constant 1 : i32
  return %0, %1 : i32, i32
}
```

The above test performs a check that after running Common Sub-Expression
elimination, only one constant remains in the IR.

#### FileCheck best practices

FileCheck is an extremely useful utility, it allows for easily matching various
parts of the output. This ease of use means that it becomes easy to write
brittle tests that are essentially `diff` tests. FileCheck tests should be as
self-contained as possible and focus on testing the minimal set of
functionalities needed. Let's see an example:

```mlir
// RUN: mlir-opt %s -cse | FileCheck %s

// CHECK-LABEL: func.func @simple_constant() -> (i32, i32)
func.func @simple_constant() -> (i32, i32) {
  // CHECK-NEXT: %result = arith.constant 1 : i32
  // CHECK-NEXT: return %result, %result : i32, i32
  // CHECK-NEXT: }

  %0 = arith.constant 1 : i32
  %1 = arith.constant 1 : i32
  return %0, %1 : i32, i32
}
```

The above example is another way to write the original example shown in the main
[FileCheck tests](#filecheck-tests) section. There are a few problems with this
test; below is a breakdown of the no-nos of this test to specifically highlight
best practices.

*   Tests should be self-contained.

This means that tests should not test lines or sections outside of what is
intended. In the above example, we see lines such as `CHECK-NEXT: }`. This line
in particular is testing pieces of the Parser/Printer of FuncOp, which is
outside of the realm of concern for the CSE pass. This line should be removed.

*   Tests should be minimal, and only check what is absolutely necessary.

This means that anything in the output that is not core to the functionality
that you are testing should *not* be present in a CHECK line. This is a separate
bullet just to highlight the importance of it, especially when checking against
IR output.

If we naively remove the unrelated `CHECK` lines in our source file, we may end
up with:

```mlir
// CHECK-LABEL: func.func @simple_constant
func.func @simple_constant() -> (i32, i32) {
  // CHECK-NEXT: %result = arith.constant 1 : i32
  // CHECK-NEXT: return %result, %result : i32, i32

  %0 = arith.constant 1 : i32
  %1 = arith.constant 1 : i32
  return %0, %1 : i32, i32
}
```

It may seem like this is a minimal test case, but it still checks several
aspects of the output that are unrelated to the CSE transformation. Namely the
result types of the `arith.constant` and `return` operations, as well the
actual SSA value names that are produced. FileCheck `CHECK` lines may contain
[regex statements](https://llvm.org/docs/CommandGuide/FileCheck.html#filecheck-regex-matching-syntax)
as well as named
[string substitution blocks](https://llvm.org/docs/CommandGuide/FileCheck.html#filecheck-string-substitution-blocks).
Utilizing the above, we end up with the example shown in the main
[FileCheck tests](#filecheck-tests) section.

```mlir
// CHECK-LABEL: func.func @simple_constant
func.func @simple_constant() -> (i32, i32) {
  /// Here we use a substitution variable as the output of the constant is
  /// useful for the test, but we omit as much as possible of everything else.
  // CHECK-NEXT: %[[RESULT:.*]] = arith.constant 1
  // CHECK-NEXT: return %[[RESULT]], %[[RESULT]]

  %0 = arith.constant 1 : i32
  %1 = arith.constant 1 : i32
  return %0, %1 : i32, i32
}
```

### Diagnostic verification tests

MLIR provides rich source location tracking that can be used to emit errors,
warnings, etc. easily from anywhere throughout the codebase. Certain classes of
tests are written to check that certain diagnostics are emitted for a given
input program, such as an MLIR file. These tests are useful in that they allow
checking specific invariants of the IR without transforming or changing
anything. Some examples of tests in this category are: those that verify
invariants of operations, or check the expected results of an analysis.
Diagnostic verification tests are written utilizing the
[source manager verifier handler](../docs/Diagnostics#sourcemgr-diagnostic-verifier-handler),
accessible via the `verify-diagnostics` flag in mlir-opt.

An example .mlir test running under `mlir-opt` is shown below:

```mlir
// RUN: mlir-opt %s -split-input-file -verify-diagnostics

// Expect an error on the same line.
func.func @bad_branch() {
  cf.br ^missing  // expected-error {{reference to an undefined block}}
}

// -----

// Expect an error on an adjacent line.
func.func @foo(%a : f32) {
  // expected-error@+1 {{invalid predicate attribute specification: "foo"}}
  %result = arith.cmpf "foo", %a, %a : f32
  return
}
```

## Unit tests

Unit tests are written using
[Google Test](https://github.com/google/googletest/blob/master/googletest/docs/primer.md)
and are located in the unittests/ directory. Tests of these form *should* be
limited to API tests that cannot be reasonably written as [Check](#check-tests)
tests, e.g. those for data structures. It is important to keep in mind that the
C++ APIs are not stable, and evolve over time. As such, directly testing the C++
IR interfaces makes the tests more fragile as those C++ APIs evolve over time.
This makes future API refactorings, which may happen frequently, much more
cumbersome as the number of tests scale.

## Integration tests

Integration tests are check tests that verify the output of MLIR code running
"end-to-end", usually by means of JIT compilation using the `mlir-cpu-runner`
utility and small runtime support library that facilates I/O. The integration
tests in MLIR don't run by default, but need to be explicitly enabled during
the initial set up described in [Getting Started](_index.md) with an
additional configuration flag.
```sh
cmake -G Ninja ../llvm \
   ... \
   -DMLIR_INCLUDE_INTEGRATION_TESTS=ON \
   ...
```
After this one-time set up, the tests run as part of regular testing as follows.
```sh
cmake --build . --target check-mlir
```
Alternatively, to just run the integration tests, the following command can be
used.
```sh
cmake --build . --target check-mlir-integration
```

The source files of the integration tests are organized within the `mlir` source
tree by dialect (for example, `test/Integration/Dialect/Vector`). Within these
directories, a `CPU` directory is used for tests that run with the
`mlir-cpu-runner` tool (this latter leaf structure may eventually disappear,
since so far all tests are cpu tests).

### Emulator

The integration tests include some tests for targets that are not widely
available yet, such as specific AVX512 features (like `vp2intersect`)
and the Intel AMX instructions. These tests require an emulator to
run correctly (lacking real hardware, of course). To enable these specific
tests, first download and install the
[Intel Emulator](https://software.intel.com/content/www/us/en/develop/articles/intel-software-development-emulator.html).
Then, include the following additional configuration flags in the initial
set up (X86Vector and AMX can be individually enabled or disabled), where
`<path to emulator>` denotes the path to the installed emulator binary.
```sh
cmake -G Ninja ../llvm \
   ... \
   -DMLIR_INCLUDE_INTEGRATION_TESTS=ON \
   -DMLIR_RUN_X86VECTOR_TESTS=ON \
   -DMLIR_RUN_AMX_TESTS=ON \
   -DINTEL_SDE_EXECUTABLE=<path to emulator> \
   ...
```
After this one-time set up, the tests run as shown earlier, but will
now include the indicated emulated tests as well.

## Command Line Incantations

While developing in MLIR, it is common to run parts of the test suite many
times. While invoking the `check-mlir` target is a nice shortcut, the
interaction with the build system can be confusing. Since most people don't
understand how all of this is put together in the build system, this section
attempts to demystify how to operate the testing tools independently.

Invoking the `check-mlir` target is roughly equivalent to running (from the
build directory):

```shell
./bin/llvm-lit tools/mlir/test
```

See the [Lit Documentation](https://llvm.org/docs/CommandGuide/lit.html) for a
description of all options.

Subsets of the testing tree can be invoked by passing a more specific path
instead of `tools/mlir/test` above. Example:

```shell
./bin/llvm-lit tools/mlir/test/Dialect/Arithmetic

# Note that it is possible to test at the file granularity, but since these
# files do not actually exist in the build directory, you need to know the
# name.
./bin/llvm-lit tools/mlir/test/Dialect/Arithmetic/ops.mlir
```

Lit has a number of options that control test execution. Here are some of the
most useful for development purposes:

* [`--filter=REGEXP`](https://llvm.org/docs/CommandGuide/lit.html#cmdoption-lit-filter) :
  Only runs tests whose name matches the REGEXP. Can also be specified via
  the `LIT_FILTER` environment variable.
* [`--filter-out=REGEXP`](https://llvm.org/docs/CommandGuide/lit.html#cmdoption-lit-filter-out) :
  Filters out tests whose name matches the REGEXP. Can also be specified via
  the `LIT_FILTER_OUT` environment variable.
* [`-a`](https://llvm.org/docs/CommandGuide/lit.html#cmdoption-lit-a) : Shows
  all information (useful while iterating on a small set of tests).
* [`--time-tests`](https://llvm.org/docs/CommandGuide/lit.html#cmdoption-lit-time-tests) :
  Prints timing statistics about slow tests and overall histograms.

Any Lit options can be set in the `LIT_OPTS` environment variable. This is
especially useful when using the build system target `check-mlir`.

Examples:

```
# Only run tests that have "python" in the name and print all invocations.
LIT_OPTS="--filter=python -a" cmake --build . --target check-mlir

# Only run the array_attributes python test, using the LIT_FILTER mechanism.
LIT_FILTER="python/ir/array_attributes" cmake --build . --target check-mlir

# Run everything except for example and integration tests (which are both
# somewhat slow).
LIT_FILTER_OUT="Examples|Integrations" cmake --build . --target check-mlir
```

Note that the above use the generic cmake command for invoking the `check-mlir`
target, but you can typically use the generator directly to be more concise
(i.e. if configured for `ninja`, then `ninja check-mlir` can replace the
`cmake --build . --target check-mlir` command). We use generic `cmake`
commands in documentation for consistency, but being concise is often better
for interactive workflows.
