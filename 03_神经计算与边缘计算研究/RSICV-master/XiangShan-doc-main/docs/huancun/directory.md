# 目录设计

本章将介绍 huancun 中目录的设计。本章中所指的“目录”是广义的，包含元数据和 Tag。

huancun 是基于目录结构的 Non-inclusive Cache，在设计过程中受到了 NCID[^ncid] 的启发。多级 Cache 之间，数据是 Non-inclusive 的，而目录则是 Inclusive 的。在结构组织上，huancun 将上层数据的目录与本地数据的目录分开存储，两者结构类似。目录使用 SRAM 搭建，以 Set 为索引，每一个 Set 中有 Way 路数据。



本地数据目录中每一项保存了如下的信息：

* state：保存该数据块的权限（Tip/Trunk/Branch/Invalid 中的一种）
* dirty：指示该数据块是否脏的
* clientStates：保存了该数据块在上层的权限情况（仅在该块非 Invalid 下有意义）
* prefetch：指示该数据块是否是被预取的



上层数据目录中每一项保存了如下的信息：

* state：保存该上层数据块的权限
* alias：保存该上层数据块的虚地址末位（即 alias bit，详见[Cache 别名问题](./cache_alias.md)）



## 目录读取

当 MSHR Alloc 模块将一个请求分配进入 MSHR 时，它也会同时向目录发起读请求。并行读取上层与本地的元数据与 Tag，根据 Tag 比对判断是否命中，依命中情况将相应路的元数据传递到对应的 MSHR 中。

目录命中时，传递的路即为命中的路；目录未命中时，传递的路是根据替换算法得到的路。替换算法可灵活配置，南湖版本本地数据目录使用 PLRU 替换算法，上层数据目录使用随机替换算法。



## 目录写入

当 MHSR 事务处理接近尾声时，通常会需要写目录以更新状态、Tag 等信息。目录有 4 个写请求端口，分别接收本地元数据、上层元数据、本地 Tag 和上层 Tag 的写入。写请求的优先级高于读请求。

连接关系上，所有 MSHR 的上述 4 种写请求分开仲裁到目录中。其中，仲裁优先级关系被精心设计以避免发生请求嵌套错误或者死锁。



## 常见问题与设计考量

#### 目录中已经有了上层元数据，为什么本地元数据中还会存 clientStates？

* 当一个请求，比如 Acquire BLOCK_A，在本地目录中 Miss 时，目录会根据替换算法选择一路的信息传递到 MSHR，此时这一路可能并不是无效的，而是有一个数据块 BLOCK_B。为了完成此 Acquire 请求，我们需要知道 BLOCK_B 在上层的状态信息。为了避免二次读目录，我们会在本地元数据中额外存一份 clientStates。



#### 目录是否会出现读写竞争冒险？

* 我们的 MSHR 是按照 Set 阻塞的，且仅当 MSHR 释放后才会让新请求进入并读取目录，因此不会出现读写竞争冒险。



[^ncid]: Zhao, Li, et al. "NCID: a non-inclusive cache, inclusive directory architecture for flexible and efficient cache hierarchies." *Proceedings of the 7th ACM international conference on Computing frontiers*. 2010.
