import torch
import torchvision.transforms as transform
from torch.utils import data
from PIL import Image
import pandas as pd
import os
import sys
import glob


def getData(mode):
    if mode == 'train':
        img_names = []
        img_classes = []
        mypath = "train_crop"
        classes = ["ALB", "BET", "DOL", "LAG", "NoF", "OTHER", "SHARK", "YFT"]
        for cl in classes:
            class_dir = mypath+'/' + cl + "/"
            filepaths = glob.glob(class_dir + "*.jpg")
            for filepath in filepaths:
                img_names.append(os.path.basename(filepath))
                # img_names.append(os.path.basename(filepath)[4:-4])
                # img_classes.append(cl)
                img_classes.append(str(classes.index(cl)))
    imgs = list(img_names)
    labels = list(img_classes)
    # imgs = list(map(int, img_names))
    # labels = list(map(int, img_classes))

    # for i in range(len(labels)):
    #     labels[i] -= 1

    # labels_tensor = torch.tensor(labels)

    return imgs, labels


class Loader(data.Dataset):
    def __init__(self, root, mode):
        self.root = root
        self.img_name, self.label = getData(mode)
        self.mode = mode
        self.length = int(len(self.img_name))
        self.transform_set = [
            transform.RandomHorizontalFlip(),
            transform.RandomVerticalFlip(),
            transform.RandomRotation(30),
            transform.ColorJitter(),
        ]
        self.transform_0 = transform.Compose([
            transform.Resize((448, 448)),
            transform.ToTensor(),
            transform.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
            #transform.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
        ])
        self.transform_n0 = transform.Compose([
            transform.Resize((448, 448)),
            transform.RandomCrop(224),
            transform.RandomHorizontalFlip(),
            transform.RandomVerticalFlip(),
            transform.RandomRotation(30),
            transform.ColorJitter(),
            transform.ToTensor(),
            transform.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
            #transform.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
        ])
        self.transform_n1 = transform.Compose([
            transform.Resize((448, 448)),
            transform.RandomCrop(224),
            transform.RandomChoice(self.transform_set),
            transform.ToTensor(),
            transform.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
            #transform.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5]),
        ])
        print(f'>> Found {self.length} {mode} images')

    def __len__(self):
        """return the size of dataset"""
        return len(self.img_name)

    def __getitem__(self, index):

        label = self.label[index]
        classes = ["ALB", "BET", "DOL", "LAG", "NoF", "OTHER", "SHARK", "YFT"]
        path = os.path.join(self.root, classes[int(label)],  str(
            self.img_name[index]).zfill(4))
        # print(path)
        img = Image.open(path).convert('RGB')
        # if label =='0':
        if label == 'test':
            img = self.transform_0(img)
        else:
            img = self.transform_n0(img)

        return img, label
