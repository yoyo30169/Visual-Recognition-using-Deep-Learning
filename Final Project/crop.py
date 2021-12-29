import cv2
import os
from os import walk
import json

with open('result.json') as f:
    data = json.load(f)
print(type(data))
print(type(data[0]))
print(data[0]['objects'][0]["relative_coordinates"]["center_x"])

for i in range(13153):
    image_name = data[i]["filename"].split('/')
    img = cv2.imread('test/'+image_name[7])
    print(image_name[7])
    if data[i]['objects'] == []:
        cv2.imwrite('test_crop/'+image_name[7], img)
        continue
    x = data[i]['objects'][0]["relative_coordinates"]["center_x"]
    y = data[i]['objects'][0]["relative_coordinates"]["center_y"]
    w = data[i]['objects'][0]["relative_coordinates"]["width"]
    h = data[i]['objects'][0]["relative_coordinates"]["height"]
    if (y-h/2) < 0:
        cropped = img[0:round(img.shape[0]*(
            y+h/2)), round(img.shape[1]*(x-w/2)): round(img.shape[1]*(x+w/2))]
    elif (x-w/2) < 0:
        cropped = img[round(img.shape[0]*(y-h/2)):round(img.shape[0]*(
            y+h/2)), 0: round(img.shape[1]*(x+w/2))]
    else:
        cropped = img[round(img.shape[0]*(y-h/2)):round(img.shape[0]*(
            y+h/2)), round(img.shape[1]*(x-w/2)): round(img.shape[1]*(x+w/2))]
    # print(img.shape[0])

    cv2.imwrite('test_crop/'+image_name[7], cropped)
