#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 10:49
# @File     : 1.开启子线程的方式一.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import time
from threading import Thread


def task(thread_name):
    print(thread_name, " is start: ", time.time())
    time.sleep(1)
    print(thread_name, " is done: ", time.time())


if __name__ == '__main__':
    thread1 = Thread(target=task, kwargs={"thread_name": "Thread 1"})
    thread1.start()
    print("Main thread is done: ", time.time())
