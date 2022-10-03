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

import requests
from bs4 import BeautifulSoup
import time

url1_1 = "https://yandex.ru/images/search?p=" 
url1_2 = "&text=polar%20bear"
url2_2 = "&text=brown%20bear"

def PictDownload (url1, url2, number, color):
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
                    image_bytes = requests.get(f'{final_link3}').content
                    time.sleep(1)
                    with open('/home/cossieman2000/WORK/python/dataset/' + str(color) + ' bear/' + str(number).zfill(4) + '.jpg', 'wb') as file:
                        file.write(image_bytes)
                    number += 1
                    time.sleep(7)
                    print(number)

number = 0
PictDownload(url1_1, url1_2, number)

number = 0
PictDownload(url1_1, url2_2, number)