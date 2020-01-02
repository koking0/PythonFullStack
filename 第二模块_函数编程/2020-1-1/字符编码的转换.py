#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/1 下午8:00
# @Author   : alex
# @File     : 字符编码的转换.py
# @Project  : PythonFullStack
# @Software : PyCharm

string = "我是Alex"
string_utf_8 = string.encode("utf-8")

print(string_utf_8)
print(string_utf_8.decode("utf-8"))