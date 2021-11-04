import torch
import torchvision.transforms as transform
from torch.utils import data
from PIL import Image
import pandas as pd
import os


def getData(mode):
    if mode == 'train':
        with open('/home/yoyo30169/VRDL dataset/datasets/training_labels.txt', 'r') as fr:
            imgs = []
            labels = []
            for line in fr:
                line = line.strip('\n')
                words = line.split()
                word1 = words[0].split('.')
                word2 = words[1].split('.')
                imgs.append(word1[0])
                labels.append(word2[0])
    imgs = list(map(int, imgs))
    labels = list(map(int, labels))
    for i in range(len(labels)):
        labels[i] -= 1

    labels_tensor = torch.tensor(labels)
    return imgs, labels_tensor


class Loader(data.Dataset):
    def __init__(self, root, mode):
        self.root = root
        self.img_name, self.label = getData(mode)
        self.mode = mode
        self.length = int(len(self.img_name))
        self.transform_0 = transform.Compose([
            transform.ToTensor(),
        ])
        self.transform_n0 = transform.Compose([
            transform.Resize((448, 448)),
            transform.RandomHorizontalFlip(),
            transform.CenterCrop(448),
            transform.ToTensor(),
            transform.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
        ])
        print(f'>> Found {self.length} {mode} images')

    def __len__(self):
        """return the size of dataset"""
        return len(self.img_name)

    def __getitem__(self, index):

        label = self.label[index]

        path = os.path.join(self.root, str(
            self.img_name[index]).zfill(4) + '.jpg')
        img = Image.open(path).convert('RGB')
        if self.mode == 'test':
            img = self.transform_0(img)
        else:
            img = self.transform_n0(img)

        return img, label
