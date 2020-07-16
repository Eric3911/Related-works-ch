
# 该项目主要研究《人脸识别处理》项目和工程

01——人脸特征提取
|
02——人脸检测
|
03——人脸对齐
|
04——活体检测
|
05——人脸比对



** 人脸识别项目工程学习流程

**一、DAN：人脸关键点检测
	ASM(Active Shape Model) 、CPR(Cascaded Pose Regression）、MTCNN 、Deep Alignment Network、landmark
	参考链接：https://mp.weixin.qq.com/s/w-ow_BP8FynTlimqBBjc8A
	
**二、人脸检测
	RetinaFace
	https://github.com/deepinsight/insightface/tree/master/RetinaFace

	FaceBoxes：—官方开源CPU实时高精度人脸检测器
	Caffe版地址：https://github.com/sfzhang15/FaceBoxes
	PyTorch版地址：https://github.com/zisianw/FaceBoxes.PyTorch
	
	ZQCNN地址：https://github.com/zuoqing1988/ZQCNN-MTCNN-vs-libfacedetection

	 libfacedetection：目前最快的人脸检测算法
	https://github.com/ShiqiYu/libfacedetection

**三、人脸对齐
	人脸对齐算法，比较传统的有ASM、AAM、CLM和一些列改进算法，而目前比较流行的有ESR、3D-ESR、SPR、LBF、SDM、CFSS等
	https://github.com/chengzhengxin/sdm
	https://github.com/1365843167/-
	https://github.com/mattzheng/Face_Swapping
	
**四、人脸识别（人脸比对/人证比对）
	https://github.com/seasonSH/DocFace
	DocFace+
	GhostVLAD
	NetVLAD
	https://www.di.ens.fr/willow/research/netvlad/

**五、刷新WIDER Face多项记录！创新奇智提出高性能精确人脸检测算法
	https://mp.weixin.qq.com/s/yrQmTxYTPKEqOHHUAt6jEg
	5.1 人脸识别损失函数
	https://mp.weixin.qq.com/s/piYyhPbA6kAXuSE5yHfQ1g
	5.2 刷新WIDER Face多项记录！创新奇智提出高性能精确人脸检测算法
	https://mp.weixin.qq.com/s/yrQmTxYTPKEqOHHUAt6jEg

**六、NINE之RetinaFace部署量化
	https://mp.weixin.qq.com/s/S04LM7Cy6KzTUAeof9fppg
