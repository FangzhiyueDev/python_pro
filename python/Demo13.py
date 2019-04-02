#!/usr/bin/python
# !coding=utf-8

import urllib.request

import time

time1 = time.time();

timePoint = int(round(time1 * 1000))

url = "http://d1.weather.com.cn/sk_2d/101020100.html?_=" + str(timePoint)

print(url)

headls = ("User-Agent", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:62.0) Gecko/20100101 Firefox/62.0");

opener = urllib.request.build_opener(headls)

opener.addheaders=[headls]

data=opener.open(url).read()


# html = urllib.request.urlopen(url)
#
# data = html.read()

htmlFile = open("subInfo.html", "wb")

htmlFile.write(data)

htmlFile.close()

print(timePoint)
