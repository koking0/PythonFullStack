#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/5 11:47
# @File     : 4.同一进程内的多个线程共享该进程的地址空间.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from threading import Thread
from multiprocessing import Process


number = 100


def task(name):
    global number
    number = 70
    print(name, " number = ", number)


if __name__ == '__main__':
    p1 = Process(target=task, args=("Process 1",))
    p1.start()
    p1.join()
    print("Under process 1, number = ", number)

    t1 = Thread(target=task, args=("Thread 1",))
    t1.start()
    t1.join()
    print("Under thread 1, number = ", number)
