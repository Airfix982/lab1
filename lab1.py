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




!pip install beautifulsoup4

import requests
from bs4 import BeautifulStoneSoup

url = "https://yandex.ru/images/search?text=polar%20bear"
r = requests.get(url)
r.content

soup = BeautifulSoup(r.content, 'html')
soup

blocks = soup.findAll('a', class_='serp-item__link')#нашли одну картинку
for block in blocks:
    print('1')
    if (block):
        download_block = block.find('img', class_='serp-item__thumb')
        if  download_block:
            fine_link = download_block.get('src')
            if  fine_link:
                print(fine_link)
                image_final_link = 'https:' + fine_link
                print(image_final_link)
            else:
                    print('no fine_link')
        else:
                print('no data-thumb')
    else:
        print('none')

print('end')