# HW3 Nuclei segmentation



Download link of Model weight:
https://drive.google.com/file/d/1W0o_AXKndNNfSdwFb5KcoDlvI3AxzUWf/view?usp=sharing

## Introdution 
1.Model
2.Reproduce submittion file

## Model
Using the Mask RCNN
Refer to the github：https://github.com/matterport/Mask_RCNN


## Reproduce submittion file
Step1:git clone Mask RCNN from https://github.com/matterport/Mask_RCNN

Step2:install Mask RCNN by command:
python setup.py install 
and download pretrained model provided by https://drive.google.com/file/d/1W0o_AXKndNNfSdwFb5KcoDlvI3AxzUWf/view?usp=sharing

Step3:use the command line to produce answer.json:
python nucleus_new.py detect --weights=mask_rcnn_nucleus_0200_resnet101.h5 --dataset=dataset --subset=test

Step4:use the transform.py to get the final answer.json and compress anwser.json to zip file.

