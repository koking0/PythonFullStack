#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 8:43
# @File     : student.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from people import People


class Student(People):
    def __init__(self, name, age, sex, id_num, password):
        super().__init__(name, age, sex, id_num, password)
        self.school = []
        self.group = []
        self.course = []

    def register(self):
        print("注册")

    def pay(self):
        print("缴费")

    def course_selection(self):
        print("选课")


if __name__ == '__main__':
    student = Student("刘兆峰", 28, "male", "20201001", "20001001")
    print(student)
