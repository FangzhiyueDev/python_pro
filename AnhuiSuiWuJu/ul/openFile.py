#!/usr/bin/python
# !coding=utf-8


from PyQt5 import QtWidgets, QtCore, QtGui, QtBluetooth
import sys
import time
import os

from AnhuiSuiWuJu.exelOprate.OprateExcel import OprateExcel
from AnhuiSuiWuJu.core import core


class FileLocalFind(QtWidgets.QWidget):
    """
    提供的是本地excel文件的查找
    """
    filePath = ""
    oprateExcel = None
    autoExec = None
    saveFileDefaultStartPath = "/home/fang/Desktop"

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.initView()

    def initView(self):
        label = QtWidgets.QLabel("请选择excel文件", self)
        label.setGeometry(100, 50, 200, 35)
        self.editFilePath = QtWidgets.QLineEdit(self)
        self.editFilePath.setGeometry(50, 100, 200, 35)
        self.editFilePath.setEnabled(False)

        openFileButton = QtWidgets.QPushButton("打开文件", self)
        openFileButton.setGeometry(250, 100, 100, 35)

        openFileButton.clicked.connect(self.fileRead)

        self.generateFilePath = QtWidgets.QLineEdit(self)
        self.generateFilePath.setGeometry(50, 200, 200, 35)
        self.generateFilePath.setEnabled(False)

        self.saveFileButton = QtWidgets.QPushButton("选择保存路径", self)
        self.saveFileButton.setGeometry(250, 200, 100, 35)

        self.saveFileButton.clicked.connect(self.saveFile)

        self.startButton = QtWidgets.QPushButton("执行", self)
        self.startButton.setGeometry(150, 250, 100, 35)
        self.startButton.clicked.connect(self.startExec)

        self.resize(400, 300)
        self.show()
        self.setFixedSize(400, 300)
        self.setWindowTitle("自动执行脚本_excel遍历文件")

    def startExec(self):
        if str(self.saveFile[0]).strip() == "" or str(self.openfile_name[0]).strip() == "":
            self.callback("请填写完整的信息")
            return
        else:
            self.oprateExcel = OprateExcel(self.openfile_name[0])

            self.oprateExcel.openFile()
            rows = self.oprateExcel.fileRows()
            for i in range(rows):
                list1 = self.oprateExcel.readFileRow(i - 1)
                self.runTask(list1)
            # 执行结束后弹出窗口
            QtWidgets.QMessageBox.information(self, "执行结果", '执行完成',
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

    def fileRead(self):
        self.openfile_name = QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', '',
                                                                   'Excel files(*.xlsx , *.xls)')  # 返回的是一个元祖(文件的路径,文件的类型)
        self.editFilePath.setText(self.openfile_name[0])

    def callback(self, error):
        reply = QtWidgets.QMessageBox.warning(self,
                                              "消息框标题",
                                              error,
                                              QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        print(reply)

    def runTask(self, list1):
        account = list1[0]
        password = list1[1]
        self.autoExec = core.AutoExec(account, password, self.saveFile[0])
        self.autoExec.exec()

    def saveFile(self):
        self.saveFile = QtWidgets.QFileDialog.getSaveFileName(self,
                                                              "文件保存",
                                                              self.saveFileDefaultStartPath,
                                                              "Excel files(*.xlsx , *.xls)")
        self.generateFilePath.setText(self.saveFile[0])
        opr = OprateExcel(self.saveFile[0])
        opr.writeInit()
        opr.writeFile(["征收项目","征收品目","年度","月份","所属期起","所属期止","纳税期限","申报期限","原申报期限",	"征收方式","纳税人"])
        opr.saveFile()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    load = FileLocalFind()
    exit(app.exec_())
