#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 8:36
# @File     : people.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import json


class People:
    def __init__(self, name, age, sex, id_num, password):
        self.name, self.age, self.sex, self.ID, self.password = name, age, sex, id_num, password

    def __str__(self):
        return json.dumps(self.__dict__)
