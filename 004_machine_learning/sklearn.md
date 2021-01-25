
1、导入sklearn的数据集模块

from sklearn import datasets

2、导入预设置的手写数据集
import matplotlib pyplot as plt

digits = datasets.load_digits()

plt.matshow(digits.images[0])
plt.show()

3、生成数据用于聚类，100个样本，2个特征，5个类别
da