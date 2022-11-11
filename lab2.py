
from lab1 import create_folder
import os
import csv
import shutil
import glob
import random

class iterator_1:
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
"""
класс итератор
"""




def write_annotation(iter1, annotation_name):
    while(True):
        try:
            photo_path = next(iter1)
            print(photo_path)
            relative_path = photo_path.split('WORK')[1]
            print(relative_path)
            class_name = relative_path.split('dataset/')[1].split(' bear')[0] + ' bear'
            print(class_name)
            with open(annotation_name, mode="a", encoding='utf-8') as write_file:
                file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow((photo_path, relative_path, class_name))
        except:
            break


    """
    Функция: Запись фалов в 1ю аннотацию
    """




def copying_dataset_1(Iter, annotation_name, new_path):
    while(1):
        try: 
            print(new_path)         
            photo_path = next(Iter)
            print(photo_path)
            half_path = photo_path.split('/dataset/')[1]
            photo_new_name = half_path.split('/')[0] + '_' + half_path.split('/')[1]
            print(photo_new_name)
            newpath = os.path.join(new_path, photo_new_name)
            print(newpath)
            shutil.copyfile(photo_path, newpath)
            relative_path = newpath.split('WORK')[1]
            class_name = half_path.split('/')[0]
            with open(annotation_name, mode="a", encoding='utf-8') as write_file:
                file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow((newpath, relative_path, class_name))
        except:
            break
        """
        Копирование фото во новый первый датасет и запись во 2ю аннотацию
        """




def copying_dataset_2(Iter, annotation_name, new_path, numbers):
    while(True):
        try: 
            print(new_path)         
            photo_path = next(Iter)
            print(photo_path)
            photo_new_name = os.path.join(new_path, str(numbers.pop(0)).zfill(5)) + '.jpg'
            newpath = os.path.join(new_path, photo_new_name)
            print(newpath)
            shutil.copyfile(photo_path, newpath)
            relative_path = newpath.split('WORK')[1]
            class_name = photo_path.split('dataset/')[1].split(' bear')[0] + ' bear'
            with open(annotation_name, mode="a", encoding='utf-8') as write_file:
                file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
                file_writer.writerow((newpath, relative_path, class_name))
        except:
            break
    """
    Функция: запись во 2ю аннотацию и копирование в новый вторый датасет
    """






if __name__=="__main__":
    path = '/home/cossieman2000/WORK/python/'
    project_name = 'dataset'
    folders = ['polar bear', 'brown bear']


    annotation_name = 'annotation_1.csv'
    filepath = os.path.join(path, annotation_name)
    with open(annotation_name, mode="w", encoding='utf-8') as write_file:
        file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
    """
    создание 1й аннотации
    """



    iter1 = iterator_1('polar bear')
    write_annotation(iter1, annotation_name)
    """
    Запись в 1ю аннотацию белых медведей
    """
    iter2 = iterator_1('brown bear')
    write_annotation(iter2, annotation_name)
    """
    Запись в 1ю аннотацию бурых медведей
    """




    project_name = 'new_data_1'
    folder = 'dataset'
    fullpath = os.path.join(path, project_name)
    create_folder(fullpath)
    new_path = os.path.join(fullpath, folder)
    create_folder(new_path)
    print(new_path)

    """
    создал новый первый датасет
    """
    annotation_name = 'annotation_2.csv'
    filepath = os.path.join(new_path, annotation_name)
    with open(annotation_name, mode="w", encoding='utf-8') as write_file:
        file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
    """
    создал 2ю аннотацию
    """




    Iter1 = iterator_1('polar bear')
    copying_dataset_1(Iter1, annotation_name, new_path)
    """
    Запись в 2ю аннотацию и копирование в 1й новый датасет белых медведей
    """
    Iter2 = iterator_1('brown bear')
    copying_dataset_1(Iter2, annotation_name, new_path)
    """
    Запись в 2ю аннотацию  и копирование в 1й новый датасет бурых медведей
    """



    project_name = 'new_data_2'
    folder = 'dataset'
    fullpath = os.path.join(path, project_name)
    create_folder(fullpath)
    new_path = os.path.join(fullpath, folder)
    create_folder(new_path)
    print(new_path)
    annotation_name = 'annotation_3.csv'
    filepath = os.path.join(new_path, annotation_name)
    with open(annotation_name, mode="w", encoding='utf-8') as write_file:
        file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
        file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
    numbers = (list(range(1,10001)))
    random.shuffle(numbers)
    """
    создание нового второго датасета и 3ей аннотации, списка рандомных чисел от 0 до 10000
    """




    Iter1 = iterator_1('polar bear')
    copying_dataset_2(Iter1, annotation_name, new_path, numbers)
    """
    запись белых медведей в 3ю аннотацию и копирование в 2й новый датасет
    """
    Iter2 = iterator_1('brown bear')
    copying_dataset_2(Iter2, annotation_name, new_path, numbers)
    """
    запись бурых медведей в 3ю аннотацию и копирование в 2й новый датасет
    """
