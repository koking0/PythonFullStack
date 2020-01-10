#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/9 下午10:32
# @Author   : alex
# @File     : 高阶函数.py
# @Project  : PythonFullStack
# @Software : PyCharm

def get_abs(n):
    return n if n > 0 else -n

def add(a, b, func):
    return func(a) + func(b)

print(add(-7, 10, get_abs))