# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/13 下午7:02
# @File     : code.py
# @Project  : PythonFullStack
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 

import re


re_ip = r'^\d{0,3}\.\d{0,3}\.\d{0,3}\.\d{0,3}'
re_time = r'[0-9]{4}:([01]\d|2[0-3]):'
re_url = r'] "(.*?) HTTP/1.1"'
re_machine = r'Mozilla/5.0 \((.*?);'

file = open("网站访问日志.txt", "r")

file_list = []
ip_dict = {}
url_dict = {}
machine_dict = {}

for (num, value) in enumerate(file):
    file_list.append([])
    file_list[num].append(re.findall(re_ip, value))
    ip_dict[str(re.findall(re_ip, value))] = ip_dict.get(str(re.findall(re_ip, value)), 0) + 1

    file_list[num].append(re.findall(re_time, value))

    file_list[num].append(re.findall(re_url, value))
    url_dict[str(re.findall(re_url, value))] = url_dict.get(str(re.findall(re_url, value)), 0) + 1

    file_list[num].append(re.findall(re_machine, value))
    machine_dict[str(re.findall(re_machine, value))] = machine_dict.get(str(re.findall(re_machine, value)), 0) + 1

print("\n页面访问量PV：")
del url_dict['[]']
url_dict = sorted(url_dict.items(), key=lambda x: x[1], reverse=True)
print(url_dict)

print("\n每个用户的访问量UV：")
del ip_dict['[]']
ip_dict = sorted(ip_dict.items(), key=lambda x: x[1], reverse=True)
print(ip_dict)

temp = {}
print("\n全天每个小时的访问量：")
for line in file_list:
    temp[int(line[1][0])] = temp.get(int(line[1][0]), 0) + 1
for i in range(24):
    print("第", i, "小时的访问量为：", temp[i])

print("\nTop 10 uv 的IP地址：")
for i in range(10):
    print(ip_dict[i])

print("\nTop 10 pv 的页面访问量：")
for i in range(10):
    print(url_dict[i])

print("\n访问来源的设备列表：")
del machine_dict['[]']
machine_dict = sorted(machine_dict.items(), key=lambda x: x[1], reverse=True)
print(machine_dict)
