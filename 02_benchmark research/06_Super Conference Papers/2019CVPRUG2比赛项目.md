
# 2019年 UG2比赛项目

个人参加这个比赛主要是测试自己的暗通道SAR及底层算法设计在质量很差的铭牌和复杂环境下识别问题

官方地址：http://www.ug2challenge.org/
本次大赛主题为“Bridging the Gap between Computational Photography and Visual Recognition”，即组织者希望研究人员关注底层的计算摄影学对高层
的视觉识别的影响，通过更加先进的手段提高“低质量成像“的视觉识别精度。比如我们熟悉的去雨、去雾、去模糊、光照增强、抗其他恶劣成像环境等，尤其是在无人机航空
影像识别场景下的研究与应用。
值得注意的是，本次挑战赛吸引了多个重量级赞助商：包括美国国家情报总监（Office of the Director of National Intelligence，ODNI）、美国情报高等研究
计划署（Intelligence Advanced Research Projects Activity ，IARPA）。

可见，美国情报的最高研究机构对无人机航空影像的重视程度它们赞助的挑战是“Video object classification and detection from unconstrained 
mobility platforms”，即非限制的移动平台视频目标分类与检测提供5万美金的总奖池！



另外来自企业界的风头正劲的互联网公司快手、美图、世界知名的传统计算机视觉技术厂商NEC和大型零售业巨头沃尔玛也进行了赞助，它们赞助的挑战是“Object 
Detection in Poor Visibility Environments”，即较差视觉环境的目标检测总奖池1万美元。


关注底层的计算摄影学对高层的视觉识别的影响通过先进手段提高“低质量成像“视觉识别精度。比如熟悉的去雨、去雾、去模糊、光照增强、抗其他恶劣成像环境等尤其是
在无人机航空影像识别场景下的研究与应用。

对于我们技术由于我们近期对SAR等遥感图像的研究和医学图像的分割采用（向量场）和（热力图）及keypoint相关研究进展我们量化测试上下采样使用不同的卷积自组织
实现我们研究初步应用测试主要问题：
  去雨、去雾、模糊、光斑、 背景复杂、小目标、 遮挡、不规则物、夜间成像的结构光和ISP问题
  
  
 航空遥感几个经典论文：
    城市图像语言分割：https://blog.csdn.net/qq_36446671/article/details/77841808
    CCF城市遥感图像分割：https://blog.csdn.net/Real_Myth/article/details/79432456
    YOLT：https://blog.csdn.net/u014380165/article/details/81556805
    船只识别：https://blog.csdn.net/baidu_32145209/article/details/82078424?utm_source=blogxgwz0
    数据集：http://levir.buaa.edu.cn/Publication.htm
    
 三种模型上采样思路
    1）STN：https://github.com/kevinzakka/spatial-transformer-network
    2）DCN
    3）DSN
    
活体指纹识别：https://arxiv.org/pdf/1905.00639.pdf 
    
