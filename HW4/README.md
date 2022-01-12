# HW4 image super resolution
Download link of model weight :

## Introduction
1.Model

2.Reproduce steps
## Model
1.EDSR

Using the EDSR Refer to the github：https://github.com/Saafke/EDSR_Tensorflow

2.SwinIR

Using the SwinIR Refer to the github：https://github.com/jingyunliang/swinir and https://github.com/cszn/KAIR

## Reproduce steps
Step1:git clone https://github.com/jingyunliang/swinir 

Step2:download model weight

Step3:use command to test:
python main_test_swinir.py --task classical_sr --scale 3 --training_patch_size 48 --model_path [model path] --folder_lq [testing images path] --folder_gt [ground truth path]

Step4:change the image names to format “00_pred.png” 


