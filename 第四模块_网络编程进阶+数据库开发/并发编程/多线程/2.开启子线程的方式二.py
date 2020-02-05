#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/4 16:36
# @File     : 2.开启子进程的方式二.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import time
from threading import Thread


class MyThread(Thread):
    def __init__(self, name):
        super(MyThread, self).__init__()
        self.name = name

    def run(self):
        print(self.name, " is start: ", time.time())
        time.sleep(2)
        print(self.name, " is done: ", time.time())


if __name__ == '__main__':
    MyThread("Thread 1").start()
    print("Main thread is done: ", time.time())

