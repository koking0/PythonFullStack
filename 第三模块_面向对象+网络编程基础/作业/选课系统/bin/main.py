#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 8:20
# @File     : main.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import os

from src.student import Student
from src.teacher import Teacher
from src.manager import Manager

menu = """
\t\t\t总菜单
\t\t1.老师登录
\t\t2.学生登录
\t\t3.学生注册
\t\t4.管理员登录
\t\t5.退出
"""


def login(identity_int):
    # 学生注册
    global obj
    if identity_int == 3:
        return Student()

    identity_dict = {
        1: "Teacher",
        2: "Student",
        4: "Manager",
    }
    id_num = input("Please input " + identity_dict[identity_int] + " id: ")
    password = input("Please input " + identity_dict[identity_int] + " password: ")

    if identity_int == 1:
        obj = Teacher(id_num)
    if identity_int == 2:
        obj = Student(id_num)
    if identity_int == 4:
        obj = Manager(id_num)

    if obj.password == password:
        return obj
    else:
        print("Wrong user name or password!")


def main():
    while True:
        print(menu)
        identity = int(input("Please input (1,2,3,4) to select login or register: ").strip())
        if identity == 5:
            exit()
        temp_obj = login(identity)
        if temp_obj:
            temp_obj.run()
