#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 8:24
# @File     : teacher.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import os
import pickle

from src.people import People

path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db\\')


class Teacher(People):
    def __init__(self, *args):
        if len(args) > 2:
            super().__init__(args[0], args[1], args[2], args[3], args[4])
            self.students, self.course = [], []
        else:
            self.load(args[0])

    def load(self, id_num):
        with open(path + "teachers.pkl", "rb") as f:
            while True:
                try:
                    temp_info = pickle.load(f)
                    if id_num == temp_info["ID"]:
                        self.__dict__ = temp_info
                except EOFError:
                    break

    def show_students(self):
        print("学员列表:")
        for student in self.students:
            print(student)

    def scoring(self):
        self.show_students()
        print("学员打分:")
        select_student = input("Please enter the student ID to be scored: ")
        score = input("Please input score: ")

        # 将新的学生信息写入学生文件
        student_list = []
        with open(path + "students.pkl", "rb") as f:
            while True:
                try:
                    flag = False
                    temp_info = pickle.load(f)
                    for course in temp_info["course"]:
                        if course["name"] in self.course and temp_info["ID"] == select_student:
                            temp_info["score"] = score
                            flag = True
                            break
                    student_list.append(temp_info)
                except EOFError:
                    break
        if flag:
            with open(path + "students.pkl", "wb") as f:
                for temp_student in student_list:
                    f.write(pickle.dumps(temp_student))
        else:
            print("Student not found！")

    def run(self):
        print("Teacher Run")
        func_menu = {
            1: "学员列表",
            2: "学员打分",
            3: "退出"
        }

        while True:
            print("讲师菜单：")
            for func in func_menu:
                print(func, func_menu[func])
            order = int(input("Please input order: "))
            if order == 1:
                self.show_students()
            if order == 2:
                self.scoring()
            if order == 3:
                return


if __name__ == '__main__':
    teacher = Teacher()
    print(teacher)
