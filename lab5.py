import torch
import numpy as np
import os
from typing import Tuple, Any

import cv2
import pandas as pd
import torchvision
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt


class CustomImageDataset(Dataset):
  def __init__(self, path_to_annotation_file: str, transform: Any=None, target_transform: Any=None) -> None:
    self.path_to_annotation_file = path_to_annotation_file
    self.dataset_info = pd.read_csv(path_to_annotation_file, header=None)
    self.dataset_info.drop(self.dataset_info.columns[[0]], axis= 1, inplace= True )
    self.dataset_info.drop (index=0, axis= 0 , inplace= True )
    self.transform = transform
    self.target_transform = target_transform

  def __len__(self) -> int:
    return len(self.dataset_info)

  def __getitem__(self, index: int) -> Tuple[torch.tensor, int]:
    path_to_image = self.dataset_info.iloc[index, 0]
    image = cv2.cvtColor(cv2.imread(path_to_image), cv2.COLOR_BGR2RGB)
    label = self.dataset_info.iloc[index, 1]

    if self.transform:
      image = self.transform(image)
    if self.target_transform:
      label = self.target_Transform(label)
      
    return image, label



path_to_dataset = r"/content/drive/MyDrive/lab5/dataset/dataset"
data_frame = pd.read_csv('annotation_2.csv')#1
data_frame.rename(columns={'Имя классa':'class_name', 'Относительный путь': 'path_to_image'}, inplace=True)
df1 = data_frame.reindex(columns=['class_name', 'path_to_image'])
df1['label'] = 0
df1.loc[df1['class_name'] == 'brown bear', 'label'] = 1
df1.loc[df1['class_name'] == 'polar bear', 'label'] = 0
df = df1[['path_to_image', 'label']]
df.to_csv(os.path.join(path_to_dataset,'annotation_2.csv'))
df['path_to_image'] = df['path_to_image'].replace(['new_data_1'], ['/content/drive/MyDrive/lab5/dataset'], regex=True)

df

custom_transforms = torchvision.transforms.Compose([torchvision.transforms.ToTensor(),
                                                    torchvision.transforms.Resize((224, 224)), 
                                                    torchvision.transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

os.path.join(path_to_dataset, "annotation_1.csv")

custom_dataset = CustomImageDataset(os.path.join(path_to_dataset, "annotation_1.csv"), custom_transforms)
custom_dataset.dataset_info

len(custom_dataset), custom_dataset[0][0].shape, custom_dataset[0][0].max(), custom_dataset[0][0].min()

custom_dataset[0][1], custom_dataset[1500][1]

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title("polar" if custom_dataset[0][1] == '0' else "brown")
plt.imshow(custom_dataset[0][0].permute(1, 2, 0).numpy()[:, :, ::-1])
plt.subplot(1, 2, 2)
plt.title("polar" if custom_dataset[1500][1] == '0' else "brown")
plt.imshow(custom_dataset[1500][0].permute(1, 2, 0).numpy()[:, :, ::-1])


from torch.utils.data import DataLoader


dataloader = DataLoader(custom_dataset, batch_size=4, shuffle=True)


plt.figure(figsize=(10, 5))

for i_batch, sample_batched in enumerate(dataloader):
    if i_batch == 1:
      break
      
    print(i_batch, sample_batched[0].shape)

    for j in range(4):
      plt.subplot(1, 4, j + 1)
      plt.title("polar" if sample_batched[1][j] == '0' else "brown")
      plt.imshow(sample_batched[0][j].permute(1, 2, 0).numpy()[:, :, ::-1])


import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms


class CNN(nn.Module):
    def __init__(self) -> None:
        super(CNN, self).__init__()
        
        self.conv_1 = nn.Conv2d(3, 16, kernel_size=3, padding=0, stride=2)
        self.conv_2 = nn.Conv2d(16, 32, kernel_size=3, padding=0, stride=2)
        self.conv_3 = nn.Conv2d(32, 64, kernel_size=3, padding=0, stride=2)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(0.1)
        self.max_pool = nn.MaxPool2d(2)
        
        self.fc_1 = nn.Linear(576, 10) # 43264 - пока что определяем экспериментальным путем (:
        self.fc_2 = nn.Linear(10, 1)
        
    def forward(self, x: torch.tensor) -> torch.tensor:
        output = self.relu(self.conv_1(x))
        output = self.max_pool(output)
        output = self.relu(self.conv_2(output))
        output = self.max_pool(output)
        output = self.relu(self.conv_3(output))
        output = self.max_pool(output)

        # print(torch.nn.Flatten()(output).shape) - определить можно, распечатав вот это

        output = torch.nn.Flatten()(output)
        output = self.relu(self.fc_1(output))
        output = torch.nn.Sigmoid()(self.fc_2(output))
        return output


import matplotlib.pyplot as plt
import numpy as np
import torch.optim as optim