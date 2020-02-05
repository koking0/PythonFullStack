#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 12:43
# @File     : 7.互斥锁.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import time
from threading import Lock
from threading import Thread


number = 100


def task():
    global number
    mutex.acquire()
    temp = number
    time.sleep(0.1)
    number = temp - 10
    mutex.release()


if __name__ == '__main__':
    mutex = Lock()
    thread_list = []
    for i in range(10):
        thread = Thread(target=task)
        thread_list.append(thread)
        thread.start()
    for thread in thread_list:
        thread.join()
    print("After thread number = ", number)