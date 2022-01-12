# HW4 image super resolution
Download link of model weight :

## Introduction
1.Model

2.Reproduce steps
## Model
1.EDSR

2.SwinIR

## Reproduce steps
Step1:git clone https://github.com/jingyunliang/swinir 

Step2:download model weight

Step3:use command to test:
python main_test_swinir.py --task classical_sr --scale 3 --training_patch_size 48 --model_path [model path] --folder_lq [testing images path] --folder_gt [ground truth path]

Step4:change the image names to format “00_pred.png” 


