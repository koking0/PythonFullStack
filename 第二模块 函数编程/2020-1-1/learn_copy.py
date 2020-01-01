#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/1 下午5:29
# @Author   : alex
# @File     : learn_copy.py
# @Project  : PythonFullStack
# @Software : PyCharm

import copy

data = {
    "name": "Alex",
    "age": "20",
    "score": {
        "离散数学": 100,
        "大学物理": 100,
        "概率论与数理统计": 100,
    }
}

data2 = data

print(data, id(data), id(data["name"]))
print(data2, id(data2), id(data2["name"]))

data2["name"] = "Jack"

print()
print(data, id(data), id(data["name"]))
print(data2, id(data2), id(data2["name"]))

data3 = data.copy()
data3["name"] = "Mike"
data3["score"]["离散数学"] = 90

print()
print(data, id(data), id(data["name"]))
print(data3, id(data3), id(data3["name"]))

data4 = copy.deepcopy(data)
data4["name"] = "Tom"
data4["score"]["离散数学"] = 80

print()
print(data, id(data), id(data["name"]))
print(data4, id(data4), id(data4["name"]))
