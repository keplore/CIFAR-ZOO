# -*-coding:utf-8-*-
# date   : 2020-1-27
# addr   : HangZhou China
# author : yangshuo
# notes  : lenet-5 pytorch code
import torch.nn as nn
import torch.nn.functional as F


__all__ = ['lenet']


class LeNet(nn.Module):
    def __init__(self, num_classes=10):
        super(LeNet, self).__init__()
        #nn.Conv2d(self, in_channels, out_channels, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True))
       #in_channel:　输入数据的通道数，例RGB图片通道数为3；
       #out_channel: 输出数据的通道数，这个根据模型调整；
       #kennel_size: 卷积核大小，可以是int，或tuple；kennel_size=2,意味着卷积大小2， kennel_size=（2,3），意味着卷积在第一维度大小为2，在第二维度大小为3；
       #stride：      步长，默认为1，与kennel_size类似，stride=2,意味在所有维度步长为2， stride=（2,3），意味着在第一维度步长为2，意味着在第二维度步长为3；
       #padding：　   零填充

        self.conv_1 = nn.Conv2d(3, 6, 5)
        self.conv_2 = nn.Conv2d(6, 16, 5)
        
        #PyTorch的nn.Linear(in_features，out_features，bias=True)是用于设置网络中的全连接层的，需要注意的是全连接层的输入与输出都是二维张量，一般形状为[batch_size, size]，
        #不同于卷积层要求输入输出是四维张量。其用法与形参说明如下：
        #in_features指的是输入的二维张量的大小，即输入的[batch_size, size]中的size。
       #out_features指的是输出的二维张量的大小，即输出的二维张量的形状为[batch_size，output_size]，当然，它也代表了该全连接层的神经元个数。
       #从输入输出的张量的shape角度来理解，相当于一个输入为[batch_size, in_features]的张量变换成了[batch_size, out_features]的输出张量。

        self.fc_1 = nn.Linear(16 * 5 * 5, 120)
        self.fc_2 = nn.Linear(120, 84)
        self.fc_3 = nn.Linear(84, num_classes)

    def forward(self, x):
        out = F.relu(self.conv_1(x))
        out = F.max_pool2d(out, 2)
        out = F.relu(self.conv_2(out))
        out = F.max_pool2d(out, 2)
        out = out.view(out.size(0), -1)
        out = F.relu(self.fc_1(out))
        out = F.relu(self.fc_2(out))
        out = self.fc_3(out)
        return out


def lenet(num_classes):
    return LeNet(num_classes=num_classes)
