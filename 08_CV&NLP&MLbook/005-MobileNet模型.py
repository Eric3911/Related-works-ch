# Author :Jungang_An
# -*- coding: utf-8 -*-
# Time : 2024/4/3 23:16

import torch
import torch.nn as nn
import torch.nn.functional as F

class DepthwiseConv2d(nn.Module):
    def __init__(self, in_channels, out_channels, kernel_size, stride, padding, dilation):
        super(DepthwiseConv2d, self).__init__()
        self.depthwise_conv = nn.Conv2d(in_channels, in_channels, kernel_size, stride, padding, dilation, groups=in_channels, bias=False)
        self.pointwise_conv = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=1, padding=0, bias=False)

    def forward(self, x):
        x = self.depthwise_conv(x)
        x = self.pointwise_conv(x)
        return x

class MobileNetV1(nn.Module):
    def __init__(self, num_classes=1000):
        super(MobileNetV1, self).__init__()
        self.layers = nn.Sequential(
            nn.Conv2d(3, 32, kernel_size=3, stride=2, padding=1),
            nn.BatchNorm2d(32),
            nn.ReLU(inplace=True),
            DepthwiseConv2d(32, 64, kernel_size=3, stride=1, padding=1, dilation=1),
            nn.BatchNorm2d(64),
            nn.ReLU(inplace=True),
            # 重复的残差块
            DepthwiseConv2d(64, 128, kernel_size=3, stride=2, padding=1, dilation=1),
            nn.BatchNorm2d(128),
            nn.ReLU(inplace=True),
            DepthwiseConv2d(128, 256, kernel_size=3, stride=2, padding=1, dilation=1),
            nn.BatchNorm2d(256),
            nn.ReLU(inplace=True),
            DepthwiseConv2d(256, 512, kernel_size=3, stride=2, padding=1, dilation=1),
            nn.BatchNorm2d(512),
            nn.ReLU(inplace=True),
            # ... 更多的残差块可以根据需要添加
            nn.AdaptiveAvgPool2d((1, 1)),
        )
        self.classifier = nn.Linear(512, num_classes)

    def forward(self, x):
        x = self.layers(x)
        x = torch.flatten(x, 1)
        x = self.classifier(x)
        return x

# 实例化模型，num_classes根据你的任务调整
model = MobileNetV1(num_classes=1000)

# 打印模型结构
print(model)