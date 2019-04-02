#! /usr/bin/python3.6
# ! coding=utf-8


import os
import sys
import pywifi
from pywifi import *


def gic():
    wifi = PyWiFi()
    ifaces = wifi.interfaces()

    for value in range(len(ifaces)):
        iface = ifaces[value]
        if iface in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]:
            print("没有链接")
        elif iface in [const.IFACE_CONNECTED]:
            print("无线的名称是=" + ifaces.name())


class PoJieWifi(object):

    def initWifiFace(self, wifiName):
        profile = pywifi.Profile()  # 创建
        profile.ssid = wifiName
        profile.auth = const.AUTH_ALG_OPEN

    def pojiePass(password):
