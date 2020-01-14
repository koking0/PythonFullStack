# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/13 下午6:51
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

STAFF_DATA = {}
STAFF_INFO = ["id", "name", "age", "phone", "dept", "enroll_date"]


# 读入员工信息
def read_staff_table():
    for i in STAFF_INFO:
        STAFF_DATA[i] = []

    with open("staff_table", "r", encoding="utf-8") as file:
        for line in file:
            staff_id, name, age, phone, dept, enroll_date = line.strip().split(",")
            STAFF_DATA["id"].append(staff_id)
            STAFF_DATA["name"].append(name)
            STAFF_DATA["age"].append(age)
            STAFF_DATA["phone"].append(phone)
            STAFF_DATA["dept"].append(dept)
            STAFF_DATA["enroll_date"].append(enroll_date)

    print_staff_table()


# 写入员工信息
def write_staff_table():
    file = open("staff_table", "w", encoding="utf-8")
    for index, _ in enumerate(STAFF_DATA["id"]):
        temp = []
        for col in STAFF_INFO:
            temp.append(STAFF_DATA[col][index])
        file.write(",".join(temp) + "\n")
    file.close()


# 打印员工信息
def print_staff_table(id_list=None, print_list=None):
    if id_list is None:
        id_list = STAFF_DATA['id']
    if print_list is None:
        print_list = STAFF_INFO
    for j in id_list:
        for i in print_list:
            print(STAFF_DATA[i][int(j) - 1], end='\t')
            if 4 < len(STAFF_DATA[i][int(j) - 1]) < 8:
                print(end='\t')
            if i == 'dept':
                if len(STAFF_DATA[i][int(j) - 1]) < 4:
                    print(end='\t\t\t')
                if len(STAFF_DATA[i][int(j) - 1]) == 5:
                    print(end='\t')
                if 5 < len(STAFF_DATA[i][int(j) - 1]) < 12:
                    print(end='\t')
        print()
    print()


# 添加员⼯信息
def add_function(order: str):
    _, _, info = order.split(' ')
    staff_list = info.split(',')
    if staff_list[2] in STAFF_DATA["phone"]:
        print("Duplicate mobile number！")
    else:
        staff_list.insert(0, len(STAFF_DATA['id']) + 1)
        for key, value in zip(STAFF_INFO, staff_list):
            STAFF_DATA[key].append(str(value))
    print_staff_table()
    write_staff_table()


# 根据序号删除相应员⼯的信息
def del_function(order: str):
    target_id = order.split(' ')[-1]
    if target_id in STAFF_DATA['id']:
        for i in STAFF_INFO:
            STAFF_DATA[i].pop(int(target_id) - 1)
        for index, _ in enumerate(STAFF_DATA['id']):
            STAFF_DATA['id'][index] = str(index + 1)
    else:
        print("The employee is not in the database!")
    print_staff_table()
    write_staff_table()


# 根据特殊条件修改员⼯信息
def update_function(order: str):
    update_info = list(re.findall(r'set (.*)=(.*) where (.*) =(.*)', order)[0])
    for index, value in enumerate(update_info):
        update_info[index] = re.sub('"', '', value).strip()

    # 1.找到符合条件的员工ID
    temp_list = []
    for index, value in enumerate(STAFF_DATA[update_info[2]]):
        if value == update_info[3]:
            temp_list.append(index)
    # 2.根据ID定位到要更改的信息
    for index in temp_list:
        STAFF_DATA[update_info[0]][index] = update_info[1]
    print_staff_table()
    write_staff_table()


# 查找员工
def find_function(order: str):
    id_list = []
    order = order.split(' ')
    for index, value in enumerate(order):
        order[index] = re.sub('"', '', value).strip()

    if order[6] == '<':
        for index, value in enumerate(STAFF_DATA[order[5]]):
            if value < order[7]:
                id_list.append(index + 1)
    if order[6] == '>':
        for index, value in enumerate(STAFF_DATA[order[5]]):
            if value > order[7]:
                id_list.append(index + 1)
    if order[6] == '=':
        for index, value in enumerate(STAFF_DATA[order[5]]):
            if value == order[7]:
                id_list.append(index + 1)
    if order[6] == 'like':
        for index, value in enumerate(STAFF_DATA[order[5]]):
            if order[7] in value:
                id_list.append(index + 1)

    print_staff_table(id_list, order[1].split(',') if order[1] != '*' else None)


# 分析输入的命令
def analysis_command(order: str):
    function_list = {
        "add": add_function,
        "del": del_function,
        "update": update_function,
        "find": find_function
    }
    if order.split(' ')[0] in function_list:
        function_list[order.split(' ')[0]](order)
    else:
        print("Illegal order！")


if __name__ == "__main__":
    read_staff_table()
    print("Welcome to the employee information inquiry program！\n\n")
    while True:
        command = input("Please input command (q to quit): ")
        if "q" in command:
            break
        analysis_command(command)
