#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/22 下午3:13
# @Author   : alex
# @File     : 股票信息查询程序.py
# @Project  : PythonFullStack
# @Software : PyCharm

def search_name(content: list, name: str):
    ans = [content[0]]      # 首先加入列表头信息
    for i in content[1:]:
        if name in str(i[2]):
            ans.append(i)
    for ans_temp in ans:
        print(ans_temp[1], "\t", ans_temp[2], "\t", ans_temp[3])


def is_number(judge_string):
    try:
        float(judge_string)
        return True
    except:
        return False


def inquiry(content: list, name: str, flag: bool, num: float):
    ans = [content[0]]      # 首先加入列表头信息
    if name == "价格":
        name = "最新价"
    index = content[0].index(name)      # 找到要筛选的列
    for temp in content[1:]:
        if is_number(temp[index]):
            if flag and float(temp[index]) > num:       # 大于判断
                ans.append(temp)
            if not flag and float(temp[index]) < num:   # 小于判断
                ans.append(temp)
    for ans_temp in ans:
        print(ans_temp[1], "\t", ans_temp[2], "\t", ans_temp[index])


file = open(file="stock_data.txt", mode="r")

file_content = []
for i in range(41):
    file_content.append(file.readline().strip().split(","))

file.close()

# print(search_name(file_content, "科技"))
# print(inquiry(file_content, "市盈率", False, 50))

print("股票信息查询系统为您服务！(输入Q退出程序)")
while True:
    order = input("请输入查询信息： ")
    if "<" in order:
        order = order.split("<")
        inquiry(file_content, order[0], False, float(order[1]))
    elif ">" in order:
        order = order.split(">")
        inquiry(file_content, order[0], True, float(order[1]))
    elif order[0] == "q" or order[0] == "Q":
        break
    else:
        search_name(file_content, order)
