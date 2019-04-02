#!/usr/bin/python3.6
# !coding=utf-8


from PyQt5.QtWidgets import *
import sys
import os


class MyTool(QWidget):
    """系统的总界面实现"""

    # asBtn, clionBtn, dgBtn, ecBtn, ecCppBtn, FzBtn, ideaBtn, ksBtn, leaNoteBtn, nodeBtn, pcBtn, slBtn, vsCodeBtn, wsBtn = None



    def __init__(self, parent=None):
        QWidget.__init__(self, parent)

        self.asBtn = QPushButton("androidStudio", self)
        self.asBtn.setGeometry(10, 10, 180, 35)
        self.asBtn.clicked.connect(self.click1)

        self.clionBtn = QPushButton("clion", self)
        self.clionBtn.setGeometry(10, 50, 180, 35)
        self.clionBtn.clicked.connect(self.click2)

        self.dgBtn = QPushButton("DataGrip", self)
        self.dgBtn.setGeometry(10, 90, 180, 35)
        self.dgBtn.clicked.connect(self.click3)

        self.ecBtn = QPushButton("eclipse", self)
        self.ecBtn.setGeometry(10, 130, 180, 35)
        self.ecBtn.clicked.connect(self.click4)

        self.webstrom = QPushButton("webstrom", self)
        self.webstrom.setGeometry(10, 170, 180, 35)
        self.webstrom.clicked.connect(self.click15)

        self.ecCppBtn = QPushButton("eclipseCpp", self)
        self.ecCppBtn.setGeometry(10, 210, 180, 35)
        self.ecCppBtn.clicked.connect(self.click6)

        self.FzBtn = QPushButton("FileZilla3", self)
        self.FzBtn.setGeometry(10, 250, 180, 35)
        self.FzBtn.clicked.connect(self.click7)

        self.ideaBtn = QPushButton("idea", self)
        self.ideaBtn.setGeometry(10, 290, 180, 35)
        self.ideaBtn.clicked.connect(self.click8)

        self.ksBtn = QPushButton("kingsoft", self)
        self.ksBtn.setGeometry(10, 330, 180, 35)
        self.ksBtn.clicked.connect(self.click9)

        self.leanote = QPushButton("leanote", self)
        self.leanote.setGeometry(10, 370, 180, 35)
        self.leanote.clicked.connect(self.click10)

        self.node = QPushButton("node.js", self)
        self.node.setGeometry(10, 410, 180, 35)
        self.node.clicked.connect(self.click11)

        self.pycharm = QPushButton("pycharm", self)
        self.pycharm.setGeometry(10, 450, 180, 35)
        self.pycharm.clicked.connect(self.click12)

        self.sublime = QPushButton("sublime", self)
        self.sublime.setGeometry(10, 490, 180, 35)
        self.sublime.clicked.connect(self.click13)

        self.vsCode = QPushButton("vsCode", self)
        self.vsCode.setGeometry(10, 530, 180, 35)
        self.vsCode.clicked.connect(self.click14)


        self.setGeometry(200, 200, 200, 590)
        self.setWindowTitle("系统工具")
        self.setMaximumHeight(590)
        self.setMaximumWidth(200)
        self.show()


# name = ["androidStudio", "clion", "DataGrip", "eclipse", "eclipseCpp", "FileZilla3", "idea", "kingsoft", "leanote",
#             "node.js", "pycharm", "sublime", "vsCode", "webstrom"]

    def click1(self):
        os.system("cd /opt/androidStudio/android-studio/bin;./studio.sh&")
        pass

    def click2(self):
        os.system("cd /opt/clion-2018.3.1/bin;./clion.sh&")
        pass

    def click3(self):
        os.system("cd /opt/DataGrip-2018.2.5/bin;./datagrip.sh&")
        pass

    def click4(self):
        os.system("cd /opt/eclipse;./eclipse&")
        pass


    def click6(self):
        os.system("cd /opt/eclipseCpp;./eclipse&")
        pass

    def click7(self):
        os.system("cd /opt/FileZilla3/bin;./filezilla&")
        pass

    def click8(self):
        os.system("cd /opt/idea-IU-183.5912.21/bin;./idea.sh&")
        pass

    def click9(self):
        os.system("cd /opt/kingsoft/wps-office/office6;./wps&")
        pass

    def click10(self):
        os.system("cd /opt/leanote;./Leanote&")
        pass

    def click11(self):
        os.system("cd /opt/node/bin;./node&")
        pass

    def click12(self):
        os.system("cd /opt/pycharm/pycharm-community-2018.2.3/bin;./pycharm.sh&")
        pass

    def click13(self):
        os.system("cd /opt/sublime_text_3;./sublime_text&")
        pass

    def click14(self):
        os.system("cd /opt/VSCode-linux-x64/bin;./code")
        pass

    def click15(self):
        os.system("cd /opt/webstrom/WebStorm-182.4323.44/bin;./webstorm.sh&")
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    load = MyTool()
    exit(app.exec_())
