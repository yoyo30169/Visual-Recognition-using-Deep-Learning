# HW2 object detection



Download link of Model weight
https://drive.google.com/file/d/1pJKRbXEu5Kffs3Lnhz2npe8AaE2LBXl_/view?usp=sharing

## Introdution 
1.Model
2.Get label
3.Implement
4.Reproduce submittion file

## Model
Using the yolov4-tiny

ˋˋˋ
123

ˋˋˋ

```
from efficientnet_pytorch import EfficientNet
model = EfficientNet.from_pretrained('efficientnet-b7')
```
Refer to the github：https://github.com/AlexeyAB/darknet

## Get label
Download the model weight and use the inference.py to reproduce answer.txt 


