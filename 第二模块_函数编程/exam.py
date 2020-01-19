#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/18 下午9:08
# @File     : exam.py
# @Project  : PythonFullStack
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 


# li = [1,2,3,5,5,6,7,8,9,9,8,3]
# temp = [x * 2 for x in li]
# print(temp)

import re

file = open("02第二模块之三体语录.txt", "r")
file_content = file.readlines()
print(file_content)
file_content.pop()
print(file_content)
file.close()

file = open("02第二模块之三体语录.txt", "w")
for i in file_content:
    file.write(i)
file.close()