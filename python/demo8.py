#!bin/usr/python
# coding=utf-8


import math
import sys

import  os


# 定义一个类

class Animal:
    '这是一个动物的基类'
    name = ""
    age = 0
    action = ""

    def __init__(self, fack):
        self.fack = fack

    def __del__(self):
        name = None


x = Animal("jainfa")
x.fack


def draColor():
    print("你好")
    return "nihao"


x.draw = draColor;

print(type(x.draw()))


class cat(Animal):
    '猫类'
    _color = ""  # 受保护的变量
    __back = ""  # 私有的变量

    def _printColor(self):
        print("猫的颜色为", self._color);

    def __printBack(self):
        print("猫的背景颜色为" + self.__back);


ca = cat();



class MyCat(cat):
    def printAbility(self):
        self._printColor();


mycat = MyCat();

