#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 8:24
# @File     : teacher.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from people import People


class Teacher(People):
    def __init__(self, name, age, sex, id_num, password):
        super().__init__(name, age, sex, id_num, password)
        self.school = []
        self.course = []

    def management_class(self):
        print("管理班级")

    def choosing_classes(self):
        print("选择班级")

    def show_students(self):
        print("查看班级学员列表")

    def scoring(self):
        print("学员打分")


if __name__ == '__main__':
    teacher = Teacher("alex", 28, "male", "20200101", "alex3714")
    print(teacher)
