#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/10 上午9:09
# @Author   : alex
# @File     : eval.py
# @Project  : PythonFullStack
# @Software : PyCharm

# names = ["alex", "coco", "lose"]
#
# f = open("eval_text.txt", "w")
# f.write(str(names))
#
# f.close()

f_ = open("eval_text.txt", "r")
cont = f_.read()
f_.close()

print(type(cont))
print(cont[5])

f_ = open("eval_text.txt", "r")

content = eval(f_.read())
print(type(content))
print(content)
f_.close()
