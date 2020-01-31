Architecure
(lenet) LeNet-5, convolutional neural networks
(alexnet) ImageNet Classification with Deep Convolutional Neural Networks
(vgg) Very Deep Convolutional Networks for Large-Scale Image Recognition
(resnet) Deep Residual Learning for Image Recognition
(preresnet) Identity Mappings in Deep Residual Networks
(resnext) Aggregated Residual Transformations for Deep Neural Networks
(densenet) Densely Connected Convolutional Networks
(senet) Squeeze-and-Excitation Networks
(bam) BAM: Bottleneck Attention Module
(cbam) CBAM: Convolutional Block Attention Module
(genet) Gather-Excite: Exploiting Feature Context in Convolutional Neural Networks
(sknet) SKNet: Selective Kernel Networks
Regularization
(shake-shake) Shake-Shake regularization
(cutout) Improved Regularization of Convolutional Neural Networks with Cutout
(mixup) mixup: Beyond Empirical Risk Minimization
Learning Rate Scheduler
(cos_lr) SGDR: Stochastic Gradient Descent with Warm Restarts
(htd_lr) Stochastic Gradient Descent with Hyperbolic-Tangent Decay on Classification

## Results on CIFAR

### Basic Architectures

| Architecture          | params | batch size | epoch | C10 test acc (%) | C100 test acc (%) |
| :-------------------- | :----: | :--------: | :---: | :--------------: | :---------------: |
| LeNet5                | 60.55K |    128     | 1000  |      76.19       |       34.10       |
| AlexNet               |  2.4M  |    128     |  250  |      75.56       |       38.67       |
| VGG19                 |  20M   |    128     |  250  |      93.00       |       72.07       |
| preresnet20           | 0.27M  |    128     |  250  |      91.88       |       67.03       |
| preresnet110          |  1.7M  |    128     |  250  |      94.24       |       72.96       |
| preresnet1202         | 19.4M  |    128     |  250  |      94.74       |       75.28       |
| densenet100bc         | 0.76M  |     64     |  300  |      95.08       |       77.55       |
| densenet190bc         | 25.6M  |     64     |  300  |      96.11       |       82.59       |
| resnext29_16x64d      | 68.1M  |    128     |  300  |      95.94       |       83.18       |
| se_resnext29_16x64d   | 68.6M  |    128     |  300  |      96.15       |     **83.65**     |
| cbam_resnext29_16x64d | 68.7M  |    128     |  300  |    **96.27**     |       83.62       |
| ge_resnext29_16x64d   | 70.0M  |    128     |  300  |      96.21       |       83.57       |


### With Additional Regularization


PS: the default data augmentation methods are ``RandomCrop`` + ``RandomHorizontalFlip`` + ``Normalize``,   
and the ``√`` means which additional method be used. :cake:

| architecture             | epoch | cutout | mixup | C10 test acc (%) |
| :----------------------- | :---: | :----: | :---: | :--------------: |
| preresnet20              |  250  |        |       |      91.88       |
| preresnet20              |  250  |   √    |       |      92.57       |
| preresnet20              |  250  |        |   √   |      92.71       |
| preresnet20              |  250  |   √    |   √   |      92.66       |
| preresnet110             |  250  |        |       |      94.24       |
| preresnet110             |  250  |   √    |       |      94.67       |
| preresnet110             |  250  |        |   √   |      94.94       |
| preresnet110             |  250  |   √    |   √   |      95.66       |
| se_resnext29_16x64d      |  300  |        |       |      96.15       |
| se_resnext29_16x64d      |  300  |   √    |       |      96.60       |
| se_resnext29_16x64d      |  300  |        |   √   |      96.86       |
| se_resnext29_16x64d      |  300  |   √    |   √   |    **97.03**     |
| cbam_resnext29_16x64d    |  300  |   √    |   √   |    **97.16**     |
| ge_resnext29_16x64d      |  300  |   √    |   √   |    **97.19**     |
| --                       |  --   |   --   |  --   |        --        |
| shake_resnet26_2x64d     | 1800  |        |       |      96.94       |
| shake_resnet26_2x64d     | 1800  |   √    |       |    **97.20**     |
| shake_resnet26_2x64d     | 1800  |        |   √   |    **97.42**     |
| **shake_resnet26_2x64d** | 1800  |   √    |   √   |    **97.71**     |

PS: ``shake_resnet26_2x64d`` achieved **97.71%** test accuracy with ``cutout`` and ``mixup``!!    
It's cool, right?  
 
### With different LR scheduler

| architecture | epoch | step decay | cosine | htd(-6,3) | cutout | mixup | C10 test acc (%) |
| :----------- | :---: | :--------: | :----: | :-------: | :----: | :---: | :--------------: |
| preresnet20  |  250  |     √      |        |           |        |       |      91.88       |
| preresnet20  |  250  |            |   √    |           |        |       |      92.13       |
| preresnet20  |  250  |            |        |     √     |        |       |      92.44       |
| preresnet20  |  250  |            |        |     √     |   √    |   √   |    **93.30**     |
| preresnet110 |  250  |     √      |        |           |        |       |      94.24       |
| preresnet110 |  250  |            |   √    |           |        |       |      94.48       |
| preresnet110 |  250  |            |        |     √     |        |       |      94.82       |
| preresnet110 |  250  |            |        |     √     |   √    |   √   |    **95.88**     |

