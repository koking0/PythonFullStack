#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/4 16:29
# @File     : 1.开启子进程的方式一.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import time
from multiprocessing import Process


def task(process_name):
    print(process_name, " is start: ", time.time())
    time.sleep(2)
    print(process_name, " is done: ", time.time())


if __name__ == '__main__':
    p = Process(target=task, kwargs={"process_name": "Process 1"})
    p.start()   # 仅仅只是给操作系统发送了一个信号
    print("Main process is done: ", time.time())
