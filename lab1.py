#import requests
#from bs4 import BeautifulStoneSoup

#url = "https://yandex.ru/images/search?text=polar%20bear"
#r = requests.get(url)
#r.text
#soup = BeautifulSoup(r.text, 'html')
#soup
#block = soup.find('div', class_='serp-item')#нашли одну картинку
#print(block)
#image_preview_link = block.find('a').get('href')
#image_preview_link
#link = 'https://yandex.ru' + image_preview_link #нашли ссылку на открытую яндекс-картинку
                                                #и перешли по ней, видим код страницы открытой картинки
#link
#r2 = requests.get(link).text
#print(r2)
#download_soup = BeautifulSoup(r2, 'html')
#download_soup
#download_block = download_soup.find('img', class_='serp-item__thumb')
#print(download_block)
#fine_link = download_block.get('data-thumb')
#print(fine_link)
#image_final_link = 'https:' + fine_link
#print(image_final_link)




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


!pip install BeautifulSoup4
import requests
from bs4 import BeautifulSoup

url = "https://yandex.ru/images/search?text=polar%20bear"
r = requests.get(url)
r.content

soup = BeautifulSoup(r.content, 'html')
soup

import time ## скачивание белых медведей, ошибка безопасного подключения
import validators
blocks = soup.findAll('div', class_='serp-item__preview')#нашли одну картинку
number = 0
for block in blocks:
    if (block):
        download_link = block.find('a', class_='serp-item__link').get('href')
        
        final_link = (download_link.split('=')[2])
        final_link1 = final_link.replace('%3A', ':')
        final_link2 = final_link1.replace('%2F', '/')
        final_link3 = (final_link2.split('&')[0])
        print(final_link3)
        if validators.url(final_link3):
            print('1')
            image_bytes = requests.get(f'{final_link3}').content
            time.sleep(1)
            with open(f'/home/cossieman2000/WORK/python/dataset/polar bear/{number}.jpg', 'wb') as file:
                file.write(image_bytes)
            number += 1
            print(number)
        else:
            continue
    #else:
    #    print('none')