---
title: "Getting Started"
date: 2019-11-29T15:26:15Z
draft: false
weight: 10
---

Don't miss the MLIR Tutorial!
[slides](https://llvm.org/devmtg/2020-09/slides/MLIR_Tutorial.pdf) -
[recording](https://www.youtube.com/watch?v=Y4SvqTtOIDk) -
[online step-by-step](https://mlir.llvm.org/docs/Tutorials/Toy/)


Please refer to the [LLVM Getting Started](https://llvm.org/docs/GettingStarted.html)
in general to build LLVM. Below are quick instructions to build MLIR with LLVM.

The following instructions for compiling and testing MLIR assume that you have
`git`, [`ninja`](https://ninja-build.org/), and a working C++ toolchain (see
[LLVM requirements](https://llvm.org/docs/GettingStarted.html#requirements)).

As a starter, you may try [the tutorial](docs/Tutorials/Toy/Ch-1.md) on
building a compiler for a Toy language.

---

**TIP**

See the
[Testing Guide - CLI Incantations](TestingGuide/#command-line-incantations)
section for additional ways to invoke and filter tests that can help you be more
efficient for regular development.

---

### Unix-like compile/testing:

```sh
git clone https://github.com/llvm/llvm-project.git
mkdir llvm-project/build
cd llvm-project/build
cmake -G Ninja ../llvm \
   -DLLVM_ENABLE_PROJECTS=mlir \
   -DLLVM_BUILD_EXAMPLES=ON \
   -DLLVM_TARGETS_TO_BUILD="Native;NVPTX;AMDGPU" \
   -DCMAKE_BUILD_TYPE=Release \
   -DLLVM_ENABLE_ASSERTIONS=ON
# Using clang and lld speeds up the build, we recommend adding:
#  -DCMAKE_C_COMPILER=clang -DCMAKE_CXX_COMPILER=clang++ -DLLVM_ENABLE_LLD=ON
# CCache can drastically speed up further rebuilds, try adding:
#  -DLLVM_CCACHE_BUILD=ON
# Optionally, using ASAN/UBSAN can find bugs early in development, enable with:
# -DLLVM_USE_SANITIZER="Address;Undefined" 
# Optionally, enabling integration tests as well
# -DMLIR_INCLUDE_INTEGRATION_TESTS=ON
cmake --build . --target check-mlir
```

It is recommended that you install `clang` and `lld` on your machine (`sudo apt-get
install clang lld` on Ubuntu for example) and uncomment the last part of the
cmake invocation above.

---

### Windows compile/testing:
To compile and test on Windows using Visual Studio 2017:

```bat
REM In shell with Visual Studio environment set up, e.g., with command such as
REM   $visual-studio-install\Auxiliary\Build\vcvarsall.bat" x64
REM invoked.
git clone https://github.com/llvm/llvm-project.git
mkdir llvm-project\build
cd llvm-project\build
cmake ..\llvm -G "Visual Studio 15 2017 Win64" -DLLVM_ENABLE_PROJECTS=mlir -DLLVM_BUILD_EXAMPLES=ON -DLLVM_TARGETS_TO_BUILD="host" -DCMAKE_BUILD_TYPE=Release -Thost=x64 -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_ASSERTIONS=ON
cmake --build . --target tools/mlir/test/check-mlir
```
