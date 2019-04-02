#!/usr/bin/python
# coding=utf-8

import pywifiTest
import time
from pywifiTest import const
from asyncio import sleep


class PoJie():
    def __init__(self, path):
        self.file = open(path, "r", errors="ignore")
        wifi = pywifiTest.PyWiFi()
        self.iface = wifi.interfaces()[0];
        self.iface.disconnect();
        time.sleep(1)
        pass


