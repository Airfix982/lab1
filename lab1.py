
import os
import requests
from bs4 import BeautifulSoup
import time
import random
#import cv2
from skimage import io

'''!pip install requests
!pip install bs4
!pip install opencv-python
!pip install scikit-image'''



def pict_download (url1: str, url2: str, number: int, color: str, fullpath: str):
    """
    функция: скачиваем фото в соответствующие папки
    """
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
                        io.imread(image_path)
                        number += 1
                        print(number)
                        image = cv2.imread(image_path)
                        cv2.imwrite(image_path, image)
                    except:
                        print('broken image')
                        continue
    print(page)

def create_folder(path: str):
        if not os.path.exists(path):
            os.mkdir(path)

if __name__=="__main__":


    url1_1 = "https://yandex.ru/images/search?p=" 
    url1_2 = "&text=polar%20bear"
    url2_2 = "&text=brown%20bear"
    path = ''
    project_name = 'dataset'
    folders = ['polar bear', 'brown bear']



    fullpath = os.path.join(path, project_name)
    print(fullpath)
    create_folder(fullpath)


    for f in folders:
        folder = os.path.join(fullpath, f)
        print(folder)
        create_folder(folder)
        """ 
        создаем папки dataset, polar bear, brown bear
        """




    number = 0
    #pict_download(url1_1, url1_2, number, 'polar', fullpath)
    """
    скачиваем белых медведей
    """

    number = 0
    #pict_download(url1_1, url2_2, number, 'brown', fullpath)
    """
    скачиваем бурых медведей
    """
