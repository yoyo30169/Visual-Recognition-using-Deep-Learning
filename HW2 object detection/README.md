# HW2 object detection



Download link of Model weight:
https://drive.google.com/file/d/1xXT-9aonHu4QSDpPJie3sexF0k8Zmz9Z/view?usp=sharing

## Introdution 
1.Model
2.Get label
3.Implement
4.Reproduce submittion file

## Model
Using the yolov4-tiny
Refer to the github：https://github.com/AlexeyAB/darknet

## Get label
Change the path which is in the `getlabels.py`
```
f = h5py.File('./train/digitStruct.mat','r')
Image.open('./train/'+IMG_NAME)
```
execute `getlabels.py` to get the ground truth label

## Implement

Step1:Git clone the darknet from(or download from) https://github.com/AlexeyAB/darknet

Step2:open the file Makefile,and modify some valus of parameters.
Change the valus of CUDNN,GPU,OPENCV from 0 to 1
```
GPU=1
CUDNN=1
OPENCV=1
```
Step3: Recompile the darknet in darknet-master directory:make
```
make
```
Step4:Preparing the data:training data,ground truth label,and some data that yolov4 needs. For example:.data and .names

Step5:After preparing all the data,we need to modify the yolov4-tiny.cfg file and start to train our own model with the yolov4-tiny pretrained model.

Step6: use this command line to train: 
./darknet detector train [HW2.data2] [yolov4-tiny.cfg] [yolov4-tiny.weights]




## Reproduce submittion file
Step1:Git clone the darknet from(or download from) https://github.com/AlexeyAB/darknet

Step2:open the file Makefile,and modify some valus of parameters.
Change the valus of CUDNN,GPU,OPENCV from 0 to 1

Step3: Recompile the darknet in darknet-master directory:make

Step4:Preparing the data:HW2.data,test.txt, yolov4-tiny.cfg and yolov4-tiny_last.weights(all provide on github)

Step5:After preparing all the data,we can use command line to produce .json file on folder “results”
./darknet detector valid cfg/HW2.data cfg/yolov4-tiny.cfg yolov4-tiny_last.weights

Step6: Change all category id:10 to 0 using transform.py code


