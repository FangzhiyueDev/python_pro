#!/bin/usr/python
# coding=utf-8

# 线程的操作

import _thread

import threading


def new_thread_method():
    print("你好")


try:
    _thread.start_new_thread(new_thread_method, ("thread1", 2))
except:
    print("错误")


# 实现继承线程实现操作

class MyThread(threading.Thread):

    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId;
        self.name = name
        self.counter = counter
        pass
