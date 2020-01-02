#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/2 下午12:04
# @Author   : alex
# @File     : decode_gbk.py
# @Project  : PythonFullStack
# @Software : PyCharm

file = open("win_data.txt", "rb")
s = file.read()
file.close()

print(s)
print(type(s))

s_utf8 = s.decode("gbk").encode("utf-8")

f = open("win_data.txt", "wb")
f.write(s_utf8)
f.close()
