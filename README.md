# HW1 image classification



Download link of Model weight
https://drive.google.com/file/d/1pJKRbXEu5Kffs3Lnhz2npe8AaE2LBXl_/view?usp=sharing

## Introdution 
1.Model
2.inference

##Model
using the pretrained Efficientnet-b7

```
from efficientnet_pytorch import EfficientNet
model = EfficientNet.from_pretrained('efficientnet-b7')
```
Refer to the github：https://github.com/lukemelas/EfficientNet-PyTorch

##inference
