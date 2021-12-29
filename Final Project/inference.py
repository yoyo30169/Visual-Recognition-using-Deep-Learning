import torchvision.transforms as transform
import os
import numpy as np
import torch
import torch.nn.functional as F
import pandas as pd
from PIL import Image
from os import walk

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def inference(imagePath, modelPath):

    classes = ["ALB", "BET", "DOL", "LAG", "NoF", "OTHER", "SHARK", "YFT"]
    inputSize = 448
    data_transforms_test = transform.Compose([
        transform.Resize(inputSize),
        transform.CenterCrop(inputSize),
        transform.RandomHorizontalFlip(),
        transform.ToTensor(),
        transform.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])

    model = torch.load(modelPath).to(device)
    model.eval()
    with torch.no_grad():
        image = Image.open(imagePath).convert('RGB')
        image_tensor = data_transforms_test(image).float()
        image_tensor = image_tensor.unsqueeze_(0).to(device)
        output = model(image_tensor)
        output = output.squeeze()
        output = F.softmax(output, dim=0)
        #score, pred_int = torch.max(output.data, 1)
        #prediction = classes[int(pred_int)]
    output = output.cpu().numpy()
    #print(score, prediction)
    print(output)
    return output


mypath = "test_crop"
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)

output = []
for img in f:
    # the predicted category
    predicted = inference('test_crop/' + img,
                          'label_result2/0.9134233518665608.pkl')
    output.append(predicted)


output = np.round(output, decimals=5)


classes = ["ALB", "BET", "DOL", "LAG", "NoF", "OTHER", "SHARK", "YFT"]

submission = pd.DataFrame(output, columns=classes)
submission.insert(0, 'image', f)


submission.to_csv('result/submission.csv', index=False)
