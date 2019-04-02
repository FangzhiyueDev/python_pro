#!/usr/bin/python
# coding=UTF-8


import math
import urllib
import json


def print_func(par):
    print("hello world", par);
    return;


def addition_func(add1, add2):
    number = add1 + add2;
    if number <= 0:
        value = 0;
    else:
        value = number;
    return value;


Money = 200;


def visit_func():
    global Money;
    Money = Money + 1;

    # print("", Money);
    # visit_func();
    # print("", Money);

    # if __name__ == '__main__':
    #     print("世界你好");

    '''
    简单的时间最基本的
    '''


class myPerson(object):
    """
    这是我的个人信息
    """
    name = ""
    age = 0
    address = ""

    def __init__(self, name, age, address):
        self.address = address
        self.age = age
        self.name = name
        pass

    def __privateFunc(self):
        print("this is private function")
        pass

    def _protectedFunc(self):
        print("this is protectes fun")
        pass

    @staticmethod
    def staticFunc():
        my = myPerson("fang", 12, "anhui")
        myPerson.staticFunc()
        pass

    @classmethod
    def classFUnc(cls):
        pass


def function1():
    print("hello world")
    pass


if __name__ == '__main__':
    # print(dir(urllib));
    # print(locals());
    # dic = locals();
    function1();
    my = myPerson("fang", 12, "sdg");
    my._protectedFunc();

    """my.__privateFUnc();
"""
pass
