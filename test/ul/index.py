#! /usr/bin/python
# ! coding=utf-8


import sys
import os
import shutil
import requests


def demo2(wd):
    response = requests.get("http://www.baidu.com", {
        "wd": wd
    })
    requests.__url__
    print(response.text)


def demo3():
    n = 5
    count = n
    n -= 1
    while n >= 1:
        count *= n
        n -= 1
        print("过程=%d" % count)

    print("计算的值=%d" % count)


import requests


def demo4():
    response=requests.get("http://www.189.cn/fj_qz/")
    textData=response.text
    file=open("/home/fang/Desktop/dianxin.html","w")
    file.write(textData)


if __name__ == '__main__':
    demo4()


def demo1():
    target = "https://www.biqukan.com/0_790/15948251.html"
    headers = {
        "Referer": "https://www.biqukan.com/0_790/",
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 62.0.3202.9Safari / 537.36"
    }
    req = requests.get(target, headers=headers)
    req.encoding = "utf-8"
    print(req.text)

    file = open("/home/fang/Desktop/book.html", "wb")
    file.write(req.content)
    print(req.text)
