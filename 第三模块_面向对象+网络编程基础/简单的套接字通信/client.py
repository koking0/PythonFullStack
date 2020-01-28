#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/22 下午3:07
# @File     : client.py
# @Project  : PythonFullStack
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 


import socket

# 1、买手机
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# print(phone)

# 2、拨号
phone.connect(('127.0.0.1', 8081))

# 3、发，收消息
phone.send('hello'.encode('utf-8'))
data = phone.recv(1024)
print(data)

# 4、关闭
phone.close()
