#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/4 16:47
# @File     : 3.查看进程pid.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import os
from multiprocessing import Process


def task(process_name):
    print(process_name, " id = ", os.getpid())
    print(process_name, " father process id = ", os.getppid())


if __name__ == '__main__':
    Process(target=task, kwargs={"process_name": "process 1"}).start()
    print("Main process id = ", os.getpid())
    print("Main process's father process id = ", os.getppid())
