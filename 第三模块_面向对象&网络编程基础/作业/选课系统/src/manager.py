#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 9:55
# @File     : manager.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from people import People


class Manager(People):
    def __init__(self, name, age, sex, id_num, password):
        super().__init__(name, age, sex, id_num, password)

    def creat_school(self):
        print("创建学校")

    def creat_group(self):
        print("创建班级")

    def creat_course(self):
        print("创建班级")

    def creat_teacher(self):
        print("创建老师")

    def creat_student(self):
        print("创建学员")


if __name__ == '__main__':
    manager = Manager("金角大王", 40, "male", "20200001", "king")
    print(manager)
