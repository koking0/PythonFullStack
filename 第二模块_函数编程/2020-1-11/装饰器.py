#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/11 下午9:19
# @Author   : alex
# @File     : 装饰器.py.py
# @Project  : PythonFullStack
# @Software : PyCharm

account = {
    "is_authenticated": False,
    "username": "Alex",
    "password": "20001001"
}


def login(func):
    def inner(*args, **kwargs):
        if account["is_authenticated"] is False:
            username = input("username:")
            password = input("password:")

            if username == account["username"] and password == account["password"]:
                print("Welcome Login...")
                account["is_authenticated"] = True
                func(*args, **kwargs)
            else:
                print("Wrong username or password!")
        else:
            print("用户已登陆。")
            func(*args, **kwargs)

    return inner


def home():
    print("---Home---")


@login
def america():
    print("---America---")


def japan():
    print("---Japan---")


@login
def hean():
    print("---Henan---")


# america = login(america)
# henan = login(henan)

home()
america()
henan()