import os

'''TO create the path file'''

TXT = './train.txt'
f1 = open(TXT, 'a')  # open file
for i in range(1, 33403):
    f1.write('/home/yoyo30169/VRDL_dataset/HW2_dataset/darknet-master/darknet-master/data/train/{}.png'.format(i))
    f1.write("\n")
f1.close()  # close file

data_listdir = os.listdir(
    "/home/yoyo30169/VRDL_dataset/HW2_dataset/darknet-master/darknet-master/data/test/test/")

TXT = './test.txt'
f1 = open(TXT, 'a')  # open file
for img_name in data_listdir:
    image_id = int(img_name[:-4])
    f1.write('/home/yoyo30169/VRDL_dataset/HW2_dataset/darknet-master/darknet-master/data/test/test/{}.png'.format(image_id))
    f1.write("\n")
f1.close()  # close file
