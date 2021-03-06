### Image Classification with CIFAR-10 and CIFAR-100
- Architecure
  - **(LeNet)** [LeNet-5, convolutional neural networks](http://yann.lecun.com/exdb/lenet/)
  - **(AlexNet)** [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper/4824-imagenet-classification-with-deep-convolutional-neural-networks)
  - **(VGG)** [Very Deep Convolutional Networks for Large-Scale Image Recognition](https://arxiv.org/abs/1409.1556)
  - **(ResNet)** [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
  - **(PreResNet)** [Identity Mappings in Deep Residual Networks](https://arxiv.org/abs/1603.05027)
  - **(ResNext)** [Aggregated Residual Transformations for Deep Neural Networks](https://arxiv.org/abs/1611.05431)
  - **(DenseNet)** [Densely Connected Convolutional Networks](https://arxiv.org/abs/1608.06993)
  - **(SENet)** [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507)
  - **(BAM)** [BAM: Bottleneck Attention Module](https://arxiv.org/abs/1807.06514)
  - **(CBAM)** [CBAM: Convolutional Block Attention Module](https://arxiv.org/abs/1807.06521)
  - **(GENet)** [Gather-Excite: Exploiting Feature Context in Convolutional Neural Networks](https://arxiv.org/abs/1810.12348)
  - **(SKNet)** [SKNet: Selective Kernel Networks](https://arxiv.org/abs/1903.06586)
- Regularization
  - **(shake-shake)** [Shake-Shake regularization](https://arxiv.org/abs/1705.07485)
  - **(cutout)** [Improved Regularization of Convolutional Neural Networks with Cutout](https://arxiv.org/abs/1708.04552)
  - **(mixup)** [mixup: Beyond Empirical Risk Minimization](https://arxiv.org/abs/1710.09412)
- Learning Rate Scheduler
  - **(cos_lr)** [SGDR: Stochastic Gradient Descent with Warm Restarts](https://arxiv.org/abs/1608.03983)
  - **(htd_lr)** [Stochastic Gradient Descent with Hyperbolic-Tangent Decay on Classification](https://arxiv.org/abs/1806.01593)

## Results on CIFAR

### Basic Architectures

| Architecture          | params | batch size | epoch | C10 test acc (%) | C100 test acc (%) |
| :-------------------- | :----: | :--------: | :---: | :--------------: | :---------------: |
| LeNet5                | 60.55K |    128     | 1000  |      75.84       |       42.10       |
| AlexNet               |  2.36M |    128     | 1000  |      76.52       |       45.25       |
| VGG19                 | 19.11M |    128     | 1000  |      93.04       |       71.51       |
| PreResNet20           |  0.26M |    128     | 1000  |      92.43       |       **.**       |
| PreResNet110          |  1.7M  |    128     | 1000  |      **.**       |       **.**       |
| PreResNet1202         | 19.4M  |    128     | 1000  |      **.**       |       **.**       |
| DenseNet100bc         | 0.76M  |    128     | 1000  |      **.**       |       **.**       |
| DenseNet190bc         | 25.6M  |    128     | 1000  |      **.**       |       **.**       |
| ResNext29_16x64d      | 68.1M  |    128     | 1000  |      **.**       |       **.**       |
| SE_ResNext29_16x64d   | 68.6M  |    128     | 1000  |      **.**       |     **83.65**     |
| shake_ResNet26_2x64d  | 68.7M  |    128     | 1000  |    **96.27**     |       **.**       |


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


