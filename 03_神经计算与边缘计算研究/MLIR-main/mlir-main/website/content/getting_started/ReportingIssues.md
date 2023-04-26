---
title: "Reporting Issues"
date: 2022-04-27T10:30:15Z
draft: false
weight: 10
---

Issues with MLIR can be reported through GitHub.  Report the issue for the
llvm-project repository at https://github.com/llvm/llvm-project/issues/new. If
possible, attach the "mlir" label (label management may be limited to accounts
that have a contribution history). Several other labels prefixed with "mlir:"
are available if the issue can be classified further, for example, "mlir:core"
can be used for issues with MLIR core libraries (`mlir/lib/IR`,
`mlir/lib/Interfaces`, etc.) and "mlir:affine" can be used for issues with MLIR
Affine dialect.  Finer-grain labels are optional.

Always provide the version of MLIR (LLVM) used. When building MLIR from source,
provide the git hash or the result of `git describe` command run in the
`llvm-project` repository.  The version reported by `mlir-opt --version` is
_insufficient_ for tools built from source.  It is sufficient from binary
"release" builds though, i.e., when not suffixed with "git".

Provide _complete_ and _minimal_ instructions to reproduce the issue.  Other
developers should be able to reproduce the issue using _only_ the code available
in MLIR repository and following the instructions provided.  Ideally, the issue
can be observed by running MLIR command-line tools (`mlir-opt`,
`mlir-translate`, etc.) on some IR.  In this case, the IR and the exact options
to the command-line tool must be provided in the issue description.  Strive to
minimize the input IR, that is, remove piece of IR that are not contributing to
the issue being triggered.  The list of command-line tool options should be
similarly minimal.  Review the [Debugging Guide](getting_started/Debugging.md)
for help on minimizing test cases.  Think of the input IR and tool options as of
a prototype for a FileCheck-based test.

When the issue cannot be reproduced using command-line tools, e.g., the issue is
related to APIs not exercised by (test) passes, provide the minimal functional
code snippet that triggers the issue along with any relevant compilation
instructions.  Think of the code snippet as of a unit test that exercises the
issue.
