#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/13 上午8:03
# @Author   : alex
# @File     : hashlib_learn.py
# @Project  : PythonFullStack
# @Software : PyCharm

import hashlib


m = hashlib.md5()
m.update(b"Hello Alex")

print(m.digest())
print(m.hexdigest())
