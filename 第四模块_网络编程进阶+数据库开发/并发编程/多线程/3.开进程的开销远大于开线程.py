#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 11:03
# @File     : 3.开进程的开销远大于开线程.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import time
from threading import Thread
from multiprocessing import Process


def task(name):
    print(name, " is start: ", time.time())
    time.sleep(2)
    print(name, " is done: ", time.time())


if __name__ == '__main__':
    process1 = Process(target=task, kwargs={"name": "Process 1"})
    process1.start()
    print("Under process 1.")

    thread1 = Thread(target=task, kwargs={"name": "Thread 1"})
    thread1.start()
    print("Under thread 1.")
