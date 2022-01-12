import os
import cv2
import pandas as pd
from PIL import Image

imagelist = os.listdir(
    '/home/yoyo30169/VRDL_dataset/HW4_dataset/datasets/training_hr_images/')

for i in imagelist:

    img_or = Image.open(
        "/home/yoyo30169/VRDL_dataset/HW4_dataset/datasets/training_hr_images/" + i)
    (w, h) = img_or.size
    print(i)

    #print('w=%d, h=%d', w, h)
    # img.show()

    new_img = img_or.resize((int(w/3), int(h/3)), Image.BICUBIC)

    # new_img.show()
    new_img.save(
        "/home/yoyo30169/VRDL_dataset/HW4_dataset/datasets/training_lr_images/" + i)
