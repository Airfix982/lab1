import os
path = '/home/cossieman2000/WORK/python/'
project_name = 'dataset'
folders = ['polar bear', 'brown bear']

def createFolder(path):
    if not os.path.exists(path):
        os.mkdir(path)

fullpath = os.path.join(path, project_name)
print(fullpath)
createFolder(fullpath)

for f in folders:
    folder = os.path.join(fullpath, f)
    print(folder)
    createFolder(folder)

!pip install requests
!pip install bs4
!pip install opencv-python

import requests
from bs4 import BeautifulSoup
import time

url1_1 = "https://yandex.ru/images/search?p=" 
url1_2 = "&text=polar%20bear"
url2_2 = "&text=brown%20bear"

import random
import cv2

import random
import cv2
from skimage import io

def PictDownload (url1, url2, number, color, fullpath):
    for page in range(0, 37):
        url = url1 + str(page) + url2
        r = requests.get(url)
        soup = BeautifulSoup(r.content, 'html')
        blocks = soup.findAll('div', class_='serp-item__preview')
        for block in blocks:
            if (block):
                download_link = block.find('a', class_='serp-item__link').get('href')               
                final_link = (download_link.split('=')[3])
                final_link1 = final_link.replace('%3A', ':')
                final_link2 = final_link1.replace('%2F', '/')
                final_link3 = (final_link2.split('&')[0])
                try:
                    final_link5 = requests.get(final_link3, timeout = 10)
                except:
                    continue
                if (final_link5.status_code == 200):
                    image_bytes = final_link5.content
                    time.sleep(random.random())
                    image_path = fullpath + '/' + str(color) + ' bear/' + str(number).zfill(4) + '.jpg'
                    print('1')
                    with open(image_path, 'wb') as file:
                        file.write(image_bytes)
                    try:
                        io.imread('/home/cossieman2000/WORK/python/dataset/polar bear/0000.jpg')
                        number += 1
                        print(number)
                        print('normal image')
                        image = cv2.imread(image_path)
                        cv2.imwrite(image_path, image)
                        print(image.shape)
                    except:
                        print('broken image')
                        continue
    print(page)

number = 0
PictDownload(url1_1, url1_2, number)

number = 0
PictDownload(url1_1, url2_2, number)

class Iterator_1:
    def __init__(self, class_name):
        print(class_name)
        self.class_name = class_name
        self.counter = 0

    def __next__(self):
        photo_path = '/home/cossieman2000/WORK/python/dataset/' + self.class_name + '/' + str(self.counter).zfill(4) + '.jpg'
        if os.path.exists(photo_path):
            self.counter += 1
            print(photo_path)
            return photo_path
        else:
            raise StopIteration

path = '/home/cossieman2000/WORK/python/'
annotation_name = 'annotation_1.csv'

filepath = os.path.join(path, annotation_name)
annotation_1 = open(filepath, "w")
annotation_1.close()

import pandas as pd

iter1 = Iterator_1('polar bear')
'''while(1):
    photo_path = next(iter1)
    print(photo_path)'''
        #abs_path = #обработать photo_path таk, ктоб тут был абсолютный путь до фото
        #rel_path = #относительный путь(только датасет и папки)
        #photo_class = #буквенное название класса(полярный или бурый медведь), и записываем в таблицу
path = '/home/cossieman2000/WORK/python/'
annotation_name = 'annotation_1.csv'

filepath = os.path.join(path, annotation_name)

def WriteAnnotation(iter1):
    #while(1):
    columns = ['absolute path', 'relative path', 'class name']
    annotation_1 = open(filepath, "a+")
    for i in range(0,5):
        #try:
        photo_path = next(iter1)
        print(photo_path)
        relative_path = photo_path.split('WORK')[1]
        print(relative_path)
        class_name = relative_path.split('dataset/')[1].split(' bear')[0] + ' bear'
        print(class_name)
        datas = [photo_path, relative_path, class_name]
        data = pd.DataFrame(datas, columns=columns)
        data.to_csv(annotation_1, mode = 'a', index = False)
        #except:
            #break
    annotation_1.close()

WriteAnnotation(iter1)