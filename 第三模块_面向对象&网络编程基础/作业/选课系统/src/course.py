#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 11:29
# @File     : course.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Course:
    def __init__(self, name, price, cycle):
        self.name = name
        self.price = price
        self.cycle = cycle

    def show_students(self):
        print("显示当前课程所有学生")
