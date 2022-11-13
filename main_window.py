#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel , QLineEdit, QHBoxLayout, QMainWindow, QInputDialog, QApplication)
from PyQt5.QtGui import QPixmap
from PyQt5 import QtWidgets
import lab2
import os
import csv


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


        self.btnAnnotation1 = QPushButton('Writing annotation', self)
        self.btnAnnotation1.move(0, 500)
        self.btnAnnotation1.clicked.connect(self.firstAnnotation)



        self.setGeometry(0, 0, 1200, 600)
        self.setWindowTitle('Application')
        self.show()

    def firstAnnotation(self):
        annotationName = 'annotation_1TEST.csv'
        with open(annotationName, mode="w", encoding='utf-8') as write_file:
            file_writer = csv.writer(write_file, delimiter = ",", lineterminator="\r")
            file_writer.writerow(('Абсолютный путь', 'Относительный путь', 'Имя классa'))
        newIter1 = lab2.iterator_1('polar bear')
        lab2.write_annotation(newIter1, annotationName)
        newIter2 = lab2.iterator_1('brown bear')
        lab2.write_annotation(newIter2, annotationName)


    def getNextBrown(self):
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