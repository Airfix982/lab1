#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QLabel , QLineEdit, QHBoxLayout, QMainWindow, QInputDialog, QApplication)
from PyQt5.QtGui import QPixmap
import lab2


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        self.btn = QPushButton('Enter path', self)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.getPath)


        self.iter1 = lab2.iterator_1('polar bear')
        picturePath = next(self.iter1)

        self.datasetPath = QLabel('path', self)
        self.datasetPath.move(130, 22)


        picture = QPixmap(picturePath)
#во 2 лабе добавить метод для предыдущей

        picture = picture.scaled(200, 200)
        lbl = QLabel(self)
        lbl.setPixmap(picture)
        lbl.move(150, 150)

        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Application')
        self.show()


    def getPath(self):

        text, ok = QInputDialog.getText(self, 'path', 'Enter the path of the dataset:')
        if ok:
            self.datasetPath.setText(str(text))


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())