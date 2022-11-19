
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
import lab2
import os
import csv
from lab1 import create_folder
import random


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.datasetPath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')


        path1 = self.datasetPath + '/brown bear'
        self.iter1 = lab2.iterator_2(path1)
        picturePath1 = next(self.iter1)
        path2 = self.datasetPath + '/polar bear'
        self.iter2 = lab2.iterator_2(path2)
        picturePath2 = next(self.iter2)    


        picture1 = QPixmap(picturePath1)
        picture1 = picture1.scaled(500, 400)
        self.lbl1 = QLabel(self)
        self.lbl1.setPixmap(picture1)
        self.lbl1.move(50, 50)
        self.btnNext1 = QPushButton('Next brown bear', self)
        self.btnNext1.move(447, 470)
        self.btnPrevious1 = QPushButton('Previous brown bear', self)
        self.btnPrevious1.move(50, 470)
        self.btnPrevious1.hide()
        self.btnNext1.clicked.connect(self.getNextBrown)
        self.btnPrevious1.clicked.connect(self.getPreviousBrown)

        picture2 = QPixmap(picturePath2)
        picture2 = picture2.scaled(500, 400)
        self.lbl2 = QLabel(self)
        self.lbl2.setPixmap(picture2)
        self.lbl2.move(630, 50)
        self.btnNext2 = QPushButton('Next polar bear', self)
        self.btnNext2.move(1035, 470)
        self.btnPrevious2 = QPushButton('Previous polar bear', self)
        self.btnPrevious2.move(630, 470)
        self.btnPrevious2.hide()
        self.btnNext2.clicked.connect(self.getNextPolar)
        self.btnPrevious2.clicked.connect(self.getPreviousPolar)


        self.btnAnnotation1 = QPushButton('first annotation', self)
        self.btnAnnotation1.move(50, 525)
        self.btnAnnotation1.clicked.connect(self.firstAnnotation)

        self.btnAnnotation2 = QPushButton('second annotation and first new dataset', self)
        self.btnAnnotation2.move(200, 525)
        self.btnAnnotation2.clicked.connect(self.secondAnnotation)

        self.btnAnnotation3 = QPushButton('third annotation and second new dataset', self)
        self.btnAnnotation3.move(500, 525)
        self.btnAnnotation3.clicked.connect(self.thirdAnnotation)



        self.setGeometry(0, 0, 1200, 600)
        self.setWindowTitle('Application')
        self.show()

    def firstAnnotation(self):
        """
        method: writing the annotation of the initial dataset
        
        """
        annotationName = 'annotation_1.csv'
        with open(annotationName, mode="w", encoding='utf-8') as write_file:
            file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
        newIter1 = lab2.iterator_1('polar bear')
        lab2.write_annotation(newIter1, annotationName)
        newIter2 = lab2.iterator_1('brown bear')
        lab2.write_annotation(newIter2, annotationName)

    def secondAnnotation(self):
        """
        method: creating the 2nd dataset;
        writing the annotation of the second dataset
        
        """
        project_name = 'new_data_1'
        folder = 'dataset'
        create_folder(project_name)
        new_path = os.path.join(project_name, folder)
        create_folder(new_path)
        print(new_path)


        annotationName = 'annotation_2.csv'
        with open(annotationName, mode="w", encoding='utf-8') as write_file:
            file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
        newIter1 = lab2.iterator_1('polar bear')
        lab2.copying_dataset_1(newIter1, annotationName, new_path)
        newIter2 = lab2.iterator_1('brown bear')
        lab2.copying_dataset_1(newIter2, annotationName, new_path)

    def thirdAnnotation(self):
        """
        method: creating the 3nd dataset;
        writing the annotation of the third dataset
        
        """
        project_name = 'new_data_2'
        folder = 'dataset'
        create_folder(project_name)
        new_path = os.path.join(project_name, folder)
        create_folder(new_path)
        print(new_path)

        
        annotation_name = 'annotation_3.csv'
        with open(annotation_name, mode="w", encoding='utf-8') as write_file:
            file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
        numbers = (list(range(1,10001)))
        random.shuffle(numbers)

        newIter1 = lab2.iterator_1('polar bear')
        lab2.copying_dataset_2(newIter1, annotation_name, new_path, numbers)
        newIter2 = lab2.iterator_1('brown bear')
        lab2.copying_dataset_2(newIter2, annotation_name, new_path, numbers)


    def getNextBrown(self):
        """
        method: getting next pictures of brown bears
        """
        picturePath = next(self.iter1)
        picture = QPixmap(picturePath).scaled(500, 400)
        self.lbl1.setPixmap(picture)
        if not (next(self.iter1)):
            self.btnNext1.hide()
        else:
            pass
        if (self.iter1.__prev__()):
            self.btnPrevious1.show()
        else:
            pass

    def getPreviousBrown(self):
        """
        method: getting privious pictures of brown bears
        """
        picturePath = self.iter1.__prev__()
        picture = QPixmap(picturePath).scaled(500, 400)
        self.lbl1.setPixmap(picture)
        if not (self.iter1.__prev__()):
            self.btnPrevious1.hide()
        else:
            pass
        if (next(self.iter1)):
            self.btnNext1.show()
        else:
            pass


    def getNextPolar(self):
        """
        method: getting next pictures of polar bears
        """
        picturePath = next(self.iter2)
        picture = QPixmap(picturePath).scaled(500, 400)
        self.lbl2.setPixmap(picture)
        if not (next(self.iter2)):
            self.btnNext2.hide()
        else:
            pass
        if (self.iter2.__prev__()):
            self.btnPrevious2.show()
        else:
            pass

    def getPreviousPolar(self):
        """
        method: getting previous pictures of polar bears
        """
        picturePath = self.iter2.__prev__()
        picture = QPixmap(picturePath).scaled(500, 400)
        self.lbl2.setPixmap(picture)
        if not (self.iter2.__prev__()):
            self.btnPrevious2.hide()
        else:
            pass
        if (next(self.iter2)):
            self.btnNext2.show()
        else:
            pass


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
