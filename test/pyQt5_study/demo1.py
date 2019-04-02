#!/usr/bin/python
# -*- coding: utf-8 -*-

# sigslot.py

import sys
from PyQt5 import QtGui, QtCore,QtWidgets


class Example(QtWidgets.QWidget):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):

        lcd = QtWidgets.QWidget.QLCDNumber(self)
        slider = QtWidgets.QWidget.QSlider(QtCore.Qt.Horizontal, self)

        vbox = QtWidgets.QWidget.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(slider)

        self.setLayout(vbox)
        self.connect(slider,  QtCore.SIGNAL('valueChanged(int)'), lcd,
            QtCore.SLOT('display(int)'))

        self.setWindowTitle('Signal & slot')
        self.resize(250, 150)


app = QtWidgets.QApplication(sys.argv)
ex = Example()
ex.show()
sys.exit(app.exec_())