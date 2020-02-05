#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 12:11
# @File     : 6.守护线程.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import time
from threading import Thread


def thread1():
    print("Thread 1 is start.")
    time.sleep(1)
    print("Thread 1 is done.")


def thread2():
    print("Thread 2 is start.")
    time.sleep(2)
    print("Thread 2 is done.")


if __name__ == '__main__':
    thread1 = Thread(target=thread1)
    thread2 = Thread(target=thread2)

    thread1.daemon = True
    thread1.start()
    thread2.start()

    print("Under thread 1 and thread 2 start.")
