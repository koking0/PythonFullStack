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
import os
import pickle

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db\\')


class Course:
    def __init__(self, *args):
        if len(args) > 1:
            self.name, self.price, self.cycle, self.place = args[0], args[1], args[2], args[3]
            self.students, self.teachers = [], []
            self.teachers.append(args[4])
        else:
            self.load(args[0])

    def load(self, name):
        with open(path + "courses.pkl", "rb") as f:
            while True:
                try:
                    temp_info = pickle.load(f)
                    if name == temp_info["name"]:
                        self.__dict__ = temp_info
                except EOFError:
                    break

    def show_students(self):
        print(self.name, " 课程学员列表：")
        for line in self.students:
            print("\t" + line)


if __name__ == '__main__':
    course = Course("python")
    course.show_students()
    print(course.__dict__)
