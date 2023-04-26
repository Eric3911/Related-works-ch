---
title: "Users of MLIR"
date: 2019-11-29T15:26:15Z
draft: false
weight: 1
---

In alphabetical order below.

## [Accera](https://github.com/microsoft/Accera)

Accera is a compiler that enables you to experiment with loop optimizations without
hand-writing Assembly code. With Accera, these problems and impediments can be
addressed in an optimized way. It is available as a Python library and supports
cross-compiling to a wide range of processor targets.

## [Beaver](https://github.com/beaver-lodge/beaver)

Beaver is an MLIR frondend in Elixir and Zig.
Powered by Elixir's composable modularity and meta-programming features,
Beaver provides a simple, intuitive, and extensible interface for MLIR.

## [CIRCT](https://github.com/llvm/circt): Circuit IR Compilers and Tools

The CIRCT project is an (experimental!) effort looking to apply MLIR and the LLVM
development methodology to the domain of hardware design tools.

## [Flang](https://github.com/llvm/llvm-project/tree/main/flang)

Flang is a ground-up implementation of a Fortran front end written in modern C++.
It started off as the [f18 project](https://github.com/flang-compiler/f18) with an
aim to replace the previous [flang project](https://github.com/flang-compiler/flang)
and address its various deficiencies. F18 was subsequently accepted into the LLVM
project and rechristened as Flang. The high level IR of the Fortran compiler is modeled
using MLIR.

## [IREE](https://github.com/google/iree)

IREE (pronounced "eerie") is a compiler and minimal runtime system for
compiling ML models for execution against a HAL (Hardware Abstraction Layer)
that is aligned with Vulkan. It aims to be a viable way to compile and run
ML devices on a variety of small and medium sized systems, leveraging either
the GPU (via Vulkan/SPIR-V), CPU or some combination. It also aims to
interoperate seamlessly with existing users of Vulkan APIs, specifically
focused on games and rendering pipelines.

## [LingoDB](https://github.com/lingo-db/lingo-db)

LingoDB is a new analytical database system that blurs the lines between databases
and compilers.


## [Lumen](https://github.com/lumen/lumen): A new compiler and runtime for BEAM languages

Lumen is not only a compiler, but a runtime as well. It consists of two parts:

- A compiler for Erlang to native code for a given target (x86, ARM, WebAssembly)
- An Erlang runtime, implemented in Rust, which provides the core functionality
  needed to implement OTP

The primary motivator for Lumen's development was the ability to compile Elixir
applications that could target WebAssembly, enabling use of Elixir as a language
for frontend development. It is also possible to use Lumen to target other
platforms as well, by producing self-contained executables on platforms such as
x86.

## [MLIR-AIE](https://github.com/Xilinx/mlir-aie): Toolchain for AMD/Xilinx AIEngine devices

MLIR-AIE is a toolchain providing low-level device configuration for Versal
AIEngine-based devices. Support is provided to target the AIEngine portion of
the device, including processors, stream switches, TileDMA and ShimDMA blocks.
Backend code generation is included, targetting the LibXAIE library, along with
some higher-level abstractions enabling higher-level design 

## [MLIR-DaCe](https://github.com/spcl/mlir-dace): Data-Centric MLIR Dialect

MLIR-DaCe is a project aiming to bridge the gap between control-centric and 
data-centric intermediate representations. By bridging these two groups of IRs, 
it allows the combination of control-centric and data-centric optimizations in 
optimization pipelines. In order to achieve this, MLIR-DaCe provides a data-centric 
dialect in MLIR to connect the MLIR and DaCe frameworks.

## [MLIR-EmitC](https://github.com/iml130/mlir-emitc)

MLIR-EmitC provides a way to translate ML models into C++ code. The repository
contains scripts and tools to translate Keras and TensorFlow models into the
[TOSA](https://mlir.llvm.org/docs/Dialects/TOSA/) and
[MHLO](https://github.com/tensorflow/mlir-hlo) dialect and to convert those to
[EmitC](https://mlir.llvm.org/docs/Dialects/EmitC/).
The latter is used to generate calls to a reference implementation.

The [EmitC](https://mlir.llvm.org/docs/Dialects/EmitC/) dialect itself, as well
as the C++ emitter, are part of MLIR core and are no longer provided as part of
the MLIR-EmitC repository.

## [Nod Distributed Runtime](https://nod.ai/project/distributedruntime/): Asynchronous fine-grained op-level parallel runtime

Nod's MLIR based Parallel Compiler and Distributed Runtime  provide a way to
easily scale out training and inference of very large models across multiple
heterogeneous devices (CPUs/GPUs/Accelerators/FPGAs)  in a cluster while
exploiting fine-grained op-level parallelism.

## [ONNX-MLIR](https://github.com/onnx/onnx-mlir)

To represent neural network models, users often use [Open Neural Network
Exchange (ONNX)](http://onnx.ai/onnx-mlir/) which is an open standard format for
machine learning interoperability.
ONNX-MLIR is a MLIR-based compiler for rewriting a model in ONNX into a standalone
binary that is executable on different target hardwares such as x86 machines,
IBM Power Systems, and IBM System Z.

See also this paper: [Compiling ONNX Neural Network Models Using
MLIR](https://arxiv.org/abs/2008.08272).

## [OpenXLA](https://github.com/openxla)

A community-driven, open source ML compiler ecosystem, using the best of XLA & MLIR.

## [PlaidML](https://github.com/plaidml/plaidml)

PlaidML is a tensor compiler that facilitates reusable and performance portable
ML models across various hardware targets including CPUs, GPUs, and
accelerators.

## [Polygeist](https://github.com/llvm/Polygeist): C/C++ frontend and optimizations for MLIR

Polygeist is a C/C++ frontend for MLIR which preserves high-level structure
from programs such as parallelism. Polygeist also includes high-level optimizations
for MLIR, as well as various raising/lowering utilities.

See both the polyhedral Polygeist paper
[Polygeist: Raising C to Polyhedral MLIR](https://ieeexplore.ieee.org/document/9563011)
and the GPU Polygeist paper
[High-Performance GPU-to-CPU Transpilation and Optimization via High-Level Parallel Constructs](https://arxiv.org/abs/2207.00257)

## [Pylir](https://github.com/zero9178/Pylir)

Pylir aims to be an optimizing Ahead-of-Time Python Compiler with high language
conformance. It uses MLIR Dialects for the task of high level, language specific
optimizations as well as LLVM for code genereation and garbage collector 
support.

## [RISE](https://rise-lang.org/)

RISE is a spiritual successor to the
[Lift project](http://www.lift-project.org/): "a high-level functional data
parallel language with a system of rewrite rules which encode algorithmic
and hardware-specific optimisation choices".

## [TFRT: TensorFlow Runtime](https://github.com/tensorflow/runtime)

TFRT aims to provide a unified, extensible infrastructure layer for an
asynchronous runtime system.

## [TensorFlow](https://www.tensorflow.org/mlir)

MLIR is used as a Graph Transformation framework and the foundation for
building many tools (XLA, TFLite converter, quantization, ...).

## [SOPHGO TPU-MLIR](https://github.com/sophgo/tpu-mlir)

TPU-MLIR is an open-source machine-learning compiler based on MLIR for
SOPHGO TPU. https://arxiv.org/abs/2210.15016.

## [Torch-MLIR](https://github.com/llvm/torch-mlir)

The Torch-MLIR project aims to provide first class compiler support from the
PyTorch ecosystem to the MLIR ecosystem.

## [Triton](https://github.com/openai/triton)

Triton is a language and compiler for writing highly efficient custom
Deep-Learning primitives. The aim of Triton is to provide an open-source
environment to write fast code at higher productivity than CUDA, but also
with higher flexibility than other existing DSLs.

## [VAST](https://github.com/trailofbits/vast): C/C++ frontend for MLIR

VAST is a library for program analysis and instrumentation of C/C++ and related languages.
VAST provides a foundation for customizable program representation for a broad spectrum
of analyses. Using the MLIR infrastructure, VAST provides a toolset to represent C/C++
program at various stages of the compilation and to transform the representation to the
best-fit program abstraction.

## [Verona](https://github.com/microsoft/verona)

Project Verona is a research programming language to explore the concept of
concurrent ownership. They are providing a new concurrency model that seamlessly
integrates ownership.
