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


def teacher_sign_in():
    pass


def student_sign_in():
    pass


def manager_sign_in():
    pass


def sign_in():
    input("Please input ")


menu = """
\t\t\t总菜单
\t\t1.老师登录
\t\t2.学生登录
\t\t3.管理员登录
"""

menu_dict = {
    "1": teacher_sign_in(),
    "2": student_sign_in(),
    "3": manager_sign_in()
}

while True:
    print(menu)
    identity = input("Please input (1,2,3) to select sign in: ").strip()
