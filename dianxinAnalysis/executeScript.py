#! /usr/bin/python
# ! coding=utf-8


import requests
import re
import os
import sys
import time


class MyDianXinDown(object):
    """
    这个类的作用是用来执行动态的下载电信官网的数据的操作，包括下载banner图片，套餐信息等相关信息，具体的操作需要根据具体的前端实现来实现

    """
    serverUrl = "http://www.189.cn"
    area = "/bj/"
    imgAddressList = set()
    saveImgAddress = "/home/fang/Desktop/downImgDir/"

    def downBannerImg(self):
        heads = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36"
        }

        response = requests.get(self.serverUrl + self.area, headers=heads)
        self.imgUrlmatch(response.text)
        for value in self.imgAddressList:
            self.downLoadImgByUrl(value)

    def imgUrlmatch(self, html):
        pattern = re.compile(r'src="(.+?\.png)"')
        m = pattern.findall(html)
        for address in m:
            if isinstance(address, str):
                if address.startswith("/upfiles/"):
                    self.imgAddressList.add(self.serverUrl + address)
                    pass

    def downLoadImgByUrl(self, url):
        heads = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.9 Safari/537.36"
        }
        name = "";
        if (isinstance(url, str)):
            name = url.split("/")[len(url.split("/")) - 1]
        response = requests.get(url=url, headers=heads)
        print(url)
        file = open(self.saveImgAddress + name, "wb")
        file.write(response.content)
        file.close()


if __name__ == '__main__':
    down = MyDianXinDown()
    down.downBannerImg()
