#!/usr/bin/python
# !coding=utf-8


import sys

from PyQt5 import QtWidgets
from AnhuiSuiWuJu.core import core


class AutoTool(QtWidgets.QWidget):
    """
    定义一个自动化工具的脚本窗体
    """

    submit = None
    user_name = None
    password = None
    reset = None

    # 自动执行脚本程序的对象
    autoExec = None

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.setGeometry(*(100, 100, 100, 100))
        self.setWindowTitle("自动化脚本")

        # 定义确定的按钮
        self.submit = QtWidgets.QPushButton("提交", self)
        self.submit.setGeometry(50, 200, 100, 35)

        self.submit.clicked.connect(self.onExec)

        # 定义重置的按钮
        self.reset = QtWidgets.QPushButton("重置", self)
        self.reset.setGeometry(250, 200, 100, 35)

        self.reset.clicked.connect(self.onReset)

        self.user_name = QtWidgets.QLineEdit(self)
        self.user_name.setGeometry(100, 50, 250, 35)

        user_label = QtWidgets.QLabel("用户名", self)
        user_label.setGeometry(50, 50, 50, 35)

        self.password = QtWidgets.QLineEdit(self)
        self.password.setGeometry(100, 100, 250, 35)

        pass_label = QtWidgets.QLabel("密码", self)
        pass_label.setGeometry(50, 100, 50, 35)
        self.resize(400, 300)
        self.show()

    def keyPressEvent(self, event):
        pass

    def onExec(self):
        if self.user_name.text().strip() == "" or self.password.text().strip() == "":
            print("请输入文字")
        else:
            self.autoExec = core.AutoExec(self.user_name.text(), self.password.text())
            self.autoExec.exec()

        # 在这里执行应用程序

        pass

    def onReset(self):
        pass


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    auto = AutoTool()
    exit(app.exec_())
