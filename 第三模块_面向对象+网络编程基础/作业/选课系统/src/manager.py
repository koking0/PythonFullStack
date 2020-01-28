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
import os
import pickle

from src.people import People
from src.teacher import Teacher
from src.course import Course


path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db\\')


class Manager(People):
    def __init__(self, *args):
        if args:
            with open(path + "managers.pkl", "rb") as f:
                while True:
                    try:
                        temp_info = pickle.load(f)
                        if temp_info["ID"] == args[0]:
                            self.__dict__ = temp_info
                    except EOFError:
                        break
        else:
            name = input("Please input manager's name: ")
            age = input("Please input manager's age: ")
            sex = input("Please input manager's sex: ")
            id_num = input("Please input manager's id: ")
            password = input("Please input manager's password: ")
            super().__init__(name, age, sex, id_num, password)

    def creat_group(self):
        print("创建班级")

    @staticmethod
    def creat_course():
        name = input("Please input course's name: ")
        price = input("Please input course's price: ")
        cycle = input("Please input course's cycle: ")
        place = input("Please input course's place: ")
        teacher = input("Please input course's teacher: ")

        with open(path + "courses.pkl", "rb") as f:
            while True:
                try:
                    temp_info = pickle.load(f)
                except EOFError:
                    break
                if name == temp_info["name"]:
                    print("Course already exists!")
                    return
        course = Course(name, price, cycle, place, teacher)
        with open(path + "courses.pkl", "ab") as f:
            f.write(pickle.dumps(course.__dict__))
        print(course.name, "create successful!")

    @staticmethod
    def creat_teacher():
        # "alex", 28, "male", "20200101", "alex3713"
        name = input("Please input teacher's name: ")
        age = input("Please input teacher's age: ")
        sex = input("Please input teacher's sex: ")
        id_num = input("Please input teacher's id: ")
        password = input("Please input teacher's password: ")

        with open(path + "teachers.pkl", "rb") as f:
            while True:
                try:
                    temp_info = pickle.load(f)
                except EOFError:
                    break
                if id_num == temp_info["ID"]:
                    print("Teacher already exists!")
                    return

        teacher = Teacher(name, age, sex, id_num, password)
        with open(path + "teachers.pkl", "ab") as f:
            f.write(pickle.dumps(teacher.__dict__))
        print(teacher.name, "create successful!")

    def run(self):
        print("Manager Run")
        func_menu = {
            1: "创建课程",
            2: "创建老师",
            3: "退出"
        }

        while True:
            print("管理员菜单：")
            for func in func_menu:
                print(func, func_menu[func])
            order = int(input("Please input order: "))
            if order == 1:
                self.creat_course()
            if order == 2:
                self.creat_teacher()
            if order == 3:
                return

#
# if __name__ == '__main__':
#     manager = Manager()
#     manager.creat_course()
