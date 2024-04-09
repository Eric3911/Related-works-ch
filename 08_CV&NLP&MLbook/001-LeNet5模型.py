# Author :Jungang_An
# -*- coding: utf-8 -*-
# Time : 2024/4/3 22:45

#LeNet-5是一个早期的卷积神经网络（CNN）架构，由Yann LeCun等人于1998年提出，被广泛应用于手写数字识别等图像识别任务。以下是一个使用Python和PyTorch库实现的LeNet-5模型的示例代码：
'''
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class LeNet5(nn.Module):
    def __init__(self):
        super(LeNet5, self).__init__()
        # 第一层卷积层，输入图像大小为32x32，输出C1特征图大小为6x6
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=0)
        # 第一个池化层，输出P2特征图大小为12x12
        self.pool1 = nn.MaxPool2d(kernel_size=2, stride=2)
        # 第二层卷积层，输出C3特征图大小为10x10
        self.conv2 = nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0)
        # 第二个池化层，输出P4特征图大小为5x5
        self.pool2 = nn.MaxPool2d(kernel_size=2, stride=2)
        # 第三层卷积层，输出C5特征图大小为4x4
        self.conv3 = nn.Conv2d(in_channels=16, out_channels=120, kernel_size=5, stride=1, padding=0)
        # 全连接层，将C5特征图展平后连接到84个节点的层
        self.fc1 = nn.Linear(120 * 4 * 4, 84)
        # 输出层，84个节点全连接到10个节点（对应10个类别）
        self.fc2 = nn.Linear(84, 10)

    def forward(self, x):
        # 通过卷积层和激活函数（ReLU）
        x = self.pool1(F.relu(self.conv1(x)))
        # 通过第二层卷积层和激活函数
        x = self.pool2(F.relu(self.conv2(x)))
        # 通过第三层卷积层
        x = self.conv3(x)
        # 展平特征图以便输入到全连接层
        x = x.view(-1, 120 * 4 * 4)
        # 通过第一个全连接层和激活函数
        x = F.relu(self.fc1(x))
        # 通过输出层得到最终的输出
        x = self.fc2(x)
        return x

# 实例化模型
model = LeNet5()

# 打印模型结构
print(model)
```
'''
#请注意，这个代码只是一个基本的LeNet-5模型实现，实际使用时可能需要根据具体的数据集和任务进行调整。例如，最后的全连接层的输出节点数（在这个例子中是10）应该与你的分类任务中的类别数相匹配。此外，你可能还需要添加正则化、dropout等技术来提高模型的泛化能力。