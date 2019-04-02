#!/usr/bin/python
# ! coding=utf-8


import os


# 操作系统接口

def demo1():
    os.getcwd()
    os.chdir(path=("/home/fang"))
    print(os.getcwd())
    dir(os)


import urllib.request


def demo2():
    content = urllib.request.urlopen("http://www.baidu.com")


def demo4():
    def demo5(pair):
        return pair[1];

    pairts = [(1, 'one'), (2, 'two'), (3, 'gewe')]
    pairts.sort(key=demo5)
    print(pairts)


def strinTest():
    string = "hello world";
    bytesO = string.encode(encoding="UTF-8")
    decode = bytesO.decode("utf-8", "strict")
    # print(decode)
    # print(bytesO)

    string.index(string, __start=0, __end=len(string))


import os
import sys


def fun2():
    list1 = ["sdgsd", 34, "sgwegwe", "sdge"]
    list1.append()


def func3():
    list1 = ["342", 45, 46, "sfgdg", {3532, "sgsd"}];
    # for event in list1.__iter__():
    #     print(event)
    # for event in list1:
    #     print(event)

    for event in list1.__iter__().__iter__().__iter__().__iter__():
        print(event)


class MyUser():
    """
    用户名信息
    """
    name = ""
    password = ""

    def __iter__(self):
        print(self.name, self.password, sep="\n")





if __name__ == '__main__':
    sys.path.append("/home/fang/python/python")
    import Demo1

    # func3()
    for attr in MyUser:
        pass
