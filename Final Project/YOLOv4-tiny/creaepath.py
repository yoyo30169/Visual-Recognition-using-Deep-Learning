import os

'''TO create the path file'''


data_listdir = os.listdir(
    "/home/yoyo30169/VRDL_dataset/Final_project/darknet/test/")

TXT = './test.txt'
f1 = open(TXT, 'a')  # open file
for img_name in data_listdir:

    f1.write(
        '/home/yoyo30169/VRDL_dataset/Final_project/darknet/test/{}'.format(img_name))
    f1.write("\n")
f1.close()  # close file
