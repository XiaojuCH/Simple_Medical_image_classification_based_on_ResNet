# -*- coding: utf-8 -*-
# @Author :Xiaoju
# Time : 2025/4/9 下午11:

import torch
import torch.nn as nn
import torchvision.models as models


class ResNet18(nn.Module):
    def __init__(self, in_channels, num_classes):
        super(ResNet18, self).__init__()
        # 加载预训练模型
        self.model = models.resnet18(pretrained=True)
        # 修改输入通道数
        if in_channels != 3:
            self.model.conv1 = nn.Conv2d(in_channels, 64, kernel_size=7, stride=2, padding=3, bias=False)
        # 修改输出层
        self.model.fc = nn.Linear(self.model.fc.in_features, num_classes)

    def forward(self, x):
        return self.model(x)


class ResNet50(nn.Module):
    def __init__(self, in_channels, num_classes):
        super(ResNet50, self).__init__()
        # 加载预训练模型
        self.model = models.resnet50(pretrained=True)
        # 修改输入通道数
        if in_channels != 3:
            self.model.conv1 = nn.Conv2d(in_channels, 64, kernel_size=7, stride=2, padding=3, bias=False)
        # 修改输出层
        self.model.fc = nn.Linear(self.model.fc.in_features, num_classes)

    def forward(self, x):
        return self.model(x)
