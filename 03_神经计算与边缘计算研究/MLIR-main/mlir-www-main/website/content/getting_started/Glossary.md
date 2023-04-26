---
title: "Glossary"
date: 2019-11-29T15:26:15Z
draft: false
weight: 30
---

This glossary contains definitions of MLIR-specific terminology. It is intended
to be a quick reference document. For terms which are well-documented elsewhere,
definitions are kept brief and the header links to the more in-depth
documentation.

<!-- When contributing, please ensure that entries remain in alphabetical order. -->

#### [Block](../docs/LangRef#blocks)

A sequential list of operations without control flow.

Also called a [basic block](https://en.wikipedia.org/wiki/Basic_block).

#### Conversion

The transformation of code represented in one dialect into a semantically
equivalent representation in another dialect (i.e. inter-dialect conversion) or
the same dialect (i.e. intra-dialect conversion).

In the context of MLIR, conversion is distinct from [translation](#translation).
Conversion refers to a transformation between (or within) dialects, but all
still within MLIR, whereas translation refers to a transformation between MLIR
and an external representation.

#### [Declarative Rewrite Rule](../docs/DeclarativeRewrites) (DRR)

A [rewrite rule](https://en.wikipedia.org/wiki/Graph_rewriting) which can be
defined declaratively (e.g. through specification in a
[TableGen](https://llvm.org/docs/TableGen/) record). At compiler build time,
these rules are expanded into an equivalent `mlir::RewritePattern` subclass.

#### [Dialect](../docs/LangRef#dialects)

A dialect is a grouping of functionality which can be used to extend the MLIR
system.

A dialect creates a unique `namespace` within which new
[operations](#operation-op), [attributes](../docs/LangRef#attributes), and
[types](../docs/LangRef#type-system) are defined. This is the fundamental method by
which to extend MLIR.

In this way, MLIR is a meta-IR: its extensible framework allows it to be
leveraged in many different ways (e.g. at different levels of the compilation
process). Dialects provide an abstraction for the different uses of MLIR while
recognizing that they are all a part of the meta-IR that is MLIR.

The tutorial provides an example of
[interfacing with MLIR](../docs/Tutorials/Toy/Ch-2#interfacing-with-mlir) in this
way.

(Note that we have intentionally selected the term "dialect" instead of
"language", as the latter would wrongly suggest that these different namespaces
define entirely distinct IRs.)

#### Export

To transform code represented in MLIR into a semantically equivalent
representation which is external to MLIR.

The tool that performs such a transformation is called an exporter.

See also: [translation](#translation).

#### [Function](../docs/LangRef#functions)

An [operation](#operation-op) with a name containing one [region](#region).

The region of a function is not allowed to implicitly capture values defined
outside of the function, and all external references must use function arguments
or attributes that establish a symbolic connection.

#### Import

To transform code represented in an external representation into a semantically
equivalent representation in MLIR.

The tool that performs such a transformation is called an importer.

See also: [translation](#translation).

#### Legalization

The process of transforming operations into a semantically equivalent
representation which adheres to the requirements set by the
[conversion target](../docs/DialectConversion#conversion-target).

That is, legalization is accomplished if and only if the new representation
contains only operations which are legal, as specified in the conversion target.

#### Lowering

The process of transforming a higher-level representation of an operation into a
lower-level, but semantically equivalent, representation.

In MLIR, this is typically accomplished through
[dialect conversion](../docs/DialectConversion). This provides a framework by which
to define the requirements of the lower-level representation, called the
[conversion target](../docs/DialectConversion#conversion-target), by specifying which
operations are legal versus illegal after lowering.

See also: [legalization](#legalization).

#### [Module](../docs/LangRef#module)

An [operation](#operation-op) which contains a single region containing a single
block that is comprised of operations.

This provides an organizational structure for MLIR operations, and is the
expected top-level operation in the IR: the textual parser returns a Module.

#### [Operation](../docs/LangRef#operations) (op)

A unit of code in MLIR. Operations are the building blocks for all code and
computations represented by MLIR. They are fully extensible (there is no fixed
list of operations) and have application-specific semantics.

An operation can have zero or more [regions](#region). Note that this creates a
nested IR structure, as regions consist of blocks, which in turn, consist of a
list of operations.

In MLIR, there are two main classes related to operations: `Operation` and `Op`.
Operation is the actual opaque instance of the operation, and represents the
general API into an operation instance. An `Op` is the base class of a derived
operation, like `ConstantOp`, and acts as smart pointer wrapper around a
`Operation*`

#### [Region](../docs/LangRef#regions)

A [CFG](https://en.wikipedia.org/wiki/Control-flow_graph) of MLIR
[blocks](#block).

#### Round-trip

The process of converting from a source format to a target format and then back
to the source format.

This is a good way of gaining confidence that the target format richly models
the source format. This is particularly relevant in the MLIR context, since
MLIR's multi-level nature allows for easily writing target dialects that model a
source format (such as TensorFlow GraphDef or another non-MLIR format)
faithfully and have a simple conversion procedure. Further cleanup/lowering can
be done entirely within the MLIR representation. This separation - making the
[importer](#import) as simple as possible and performing all further
cleanups/lowering in MLIR - has proven to be a useful design pattern.

#### [Terminator operation](../docs/LangRef#control-flow-and-ssacfg-regions)

An [operation](#operation-op) which *must* terminate a [block](#block).
Terminator operations are a special category of operations.

#### Transitive lowering

An A->B->C [lowering](#lowering); that is, a lowering in which multiple patterns
may be applied in order to fully transform an illegal operation into a set of
legal ones.

This provides the flexibility that the [conversion](#conversion) framework may
perform the lowering in multiple stages of applying patterns (which may utilize
intermediate patterns not in the conversion target) in order to fully legalize
an operation. This is accomplished through
[partial conversion](../docs/DialectConversion#modes-of-conversion).

#### Translation

The transformation of code represented in an external (non-MLIR) representation
into a semantically equivalent representation in MLIR (i.e.
[importing](#import)), or the inverse (i.e. [exporting](#export)).

In the context of MLIR, translation is distinct from [conversion](#conversion).
Translation refers to a transformation between MLIR and an external
representation, whereas conversion refers to a transformation within MLIR
(between or within dialects).
