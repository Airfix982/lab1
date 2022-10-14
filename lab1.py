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