---
date: 2017-10-19T15:26:15Z
lastmod: 2019-10-26T15:26:15Z
publishdate: 2018-11-23T15:26:15Z
---

# Multi-Level Intermediate Representation Overview

The MLIR project is a novel approach to building reusable and extensible
compiler infrastructure. MLIR aims to address software fragmentation, improve
compilation for heterogeneous hardware, significantly reduce the cost of
building domain specific compilers, and aid in connecting existing compilers
together.

# Weekly Public Meeting

We host a **weekly public meeting** about MLIR and the ecosystem.
To be notified of the next meeting, please subscribe to the
[MLIR Announcements](https://discourse.llvm.org/c/mlir/mlir-announcements/44)
category on Discourse.

You can register to [this public calendar](https://calendar.google.com/calendar/u/0?cid=N2EzMDU3NTBjMjkzYWU5MTY5NGNlMmQ3YjJlN2JjNWEyYjViNjg1NTRmODcxOWZiOTU1MmIzNGQxYjkwNGJkZEBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)
to keep up-to-date with the schedule. 

If you’d like to discuss a particular topic or have questions, please add it to the
[agenda doc](https://docs.google.com/document/d/1y2YlcOVMPocQjSFi3X6gYGRjA0onyqr41ilXji10phw/edit#).

The meetings are recorded and published in the [talks](talks/) section.


## More resources

For more information on MLIR, please see:

*   The MLIR section of the [LLVM forums](https://llvm.discourse.group/c/mlir/31) for any questions.
*   Real-time discussion on the MLIR channel of the [LLVM discord](https://discord.gg/xS7Z362) server.
*   Previous [talks](talks/).

## What is MLIR for?

MLIR is intended to be a hybrid IR which can support multiple different
requirements in a unified infrastructure. For example, this includes:

*   The ability to represent dataflow graphs (such as in TensorFlow), including
    dynamic shapes, the user-extensible op ecosystem, TensorFlow variables, etc.
*   Optimizations and transformations typically done on such graphs (e.g. in
    Grappler).
*   Ability to host high-performance-computing-style loop optimizations across
    kernels (fusion, loop interchange, tiling, etc.), and to transform memory
    layouts of data.
*   Code generation "lowering" transformations such as DMA insertion, explicit
    cache management, memory tiling, and vectorization for 1D and 2D register
    architectures.
*   Ability to represent target-specific operations, e.g. accelerator-specific
    high-level operations.
*   Quantization and other graph transformations done on a Deep-Learning graph.
*   [Polyhedral primitives](/docs/Dialects/Affine/).
*   [Hardware Synthesis Tools / HLS](https://circt.llvm.org).

MLIR is a common IR that also supports hardware specific operations. Thus,
any investment into the infrastructure surrounding MLIR (e.g. the compiler
passes that work on it) should yield good returns; many targets can use that
infrastructure and will benefit from it.

MLIR is a powerful representation, but it also has non-goals. We do not try to
support low level machine code generation algorithms (like register allocation
and instruction scheduling). They are a better fit for lower level optimizers
(such as LLVM). Also, we do not intend MLIR to be a source language that
end-users would themselves write kernels in (analogous to CUDA C++). On the
other hand, MLIR provides the backbone for representing any such DSL and
integrating it in the ecosystem.

## Compiler infrastructure

We benefited from experience gained from building other IRs (LLVM IR, XLA HLO,
and Swift SIL) when building MLIR. The MLIR framework encourages existing
best practices, e.g. writing and maintaining an IR spec, building an IR verifier,
providing the ability to dump and parse MLIR files to text, writing extensive
unit tests with the [FileCheck](https://llvm.org/docs/CommandGuide/FileCheck.html)
tool, and building the infrastructure as a set of modular libraries that can be
combined in new ways.

Other lessons have been incorporated and integrated into the design in subtle
ways. For example, LLVM has non-obvious design mistakes that prevent a
multithreaded compiler from working on multiple functions in an LLVM module at
the same time. MLIR solves these problems by having limited SSA scope to reduce
the use-def chains and by replacing cross-function references with explicit
[`symbol reference`](docs/LangRef/#symbol-reference-attribute).

## Citing MLIR

Please see the [FAQ
entry](https://mlir.llvm.org/getting_started/Faq/#how-to-refer-to-mlir-in-publications-is-there-an-accompanying-paper)
on how to cite MLIR in publications.
