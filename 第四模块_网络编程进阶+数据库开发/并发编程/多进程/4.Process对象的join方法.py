#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/4 21:21
# @File     : 4.Process对象的join方法.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import time
import multiprocessing


def task(process_name, sleep_time):
    print(process_name, " is start: ", time.time())
    time.sleep(sleep_time)


if __name__ == '__main__':
    start = time.time()
    process1 = multiprocessing.Process(target=task, kwargs={"process_name": "process1", "sleep_time": 1})
    process2 = multiprocessing.Process(target=task, kwargs={"process_name": "process2", "sleep_time": 2})
    process3 = multiprocessing.Process(target=task, kwargs={"process_name": "process3", "sleep_time": 3})
    process4 = multiprocessing.Process(target=task, kwargs={"process_name": "process4", "sleep_time": 4})

    process1.start()
    process2.start()
    print("After process1 and process2 start.")
    process1.join()
    process2.join()

    print("Time1 = ", time.time() - start)
    print("Process1 pid = ", process1.pid)      # 僵尸进程
    print("Process2 is live: ", process2.is_alive())

    process3.start()
    process3.terminate()
    print("Process3 is live: ", process3.is_alive())
    time.sleep(1)
    print("Process3 is live: ", process3.is_alive())
    process3.join()

    process4.start()
    process4.join()

    print("Time2 = ", time.time() - start)
