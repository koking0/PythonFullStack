#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 8:24
# @File     : group.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Group:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def show_students(self):
        print("显示当前班级所有学生")

