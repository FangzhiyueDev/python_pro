#!/usr/bin/python
# !coding=utf-8


from PyQt5 import QtWidgets, QtCore, QtGui, QtBluetooth
import sys
import time
import os


class FileLocalFind(QtWidgets.QWidget):
    """
    提供的是本地excel文件的查找
    """
    filePath = ""

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.initView()

    def initView(self):
        self.resize(400, 400)
        self.show()
        self.setWindowTitle("自动执行脚本_excel遍历文件")

        editFilePath=QtWidgets.QLineEdit("文件路径",self)
        editFilePath.setGeometry(100,100,100,35)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    load = FileLocalFind()
    exit(app.exec_())
