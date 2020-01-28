#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/26 8:43
# @File     : student.py
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

db_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'db\\')


class Student(People):
    def __init__(self, *args):
        if args:
            with open(db_path + "students.pkl", "rb") as f:
                while True:
                    try:
                        temp_info = pickle.load(f)
                        if temp_info["ID"] == args[0]:
                            self.__dict__ = temp_info
                            if not hasattr(self, "course"):
                                self.course = []
                    except EOFError:
                        break
        else:
            self.creat_student()
            self.course = []

    def creat_student(self):
        # name, age, sex, id_num, password = "Alex", 18, "male", "1001", "20001001"
        name = input("Please input student's name: ")
        age = input("Please input student's age: ")
        sex = input("Please input student's sex: ")
        id_num = input("Please input student's(must start with 10) id: ")
        password = input("Please input student's password: ")

        with open(db_path + "students.pkl", "rb") as f:
            while True:
                try:
                    temp_info = pickle.load(f)
                except EOFError:
                    break
                if id_num == temp_info["ID"]:
                    print("User already exists!")

        super().__init__(name, age, sex, id_num, password)
        with open(db_path + "students.pkl", "ab") as f:
            f.write(pickle.dumps(self.__dict__))

    def course_selection(self):
        course_list = []

        # 打印可选课程列表。
        print("课程名\t\t价格\t\t周期")
        with open(db_path + "courses.pkl", "rb") as f:
            while True:
                try:
                    temp_info = pickle.load(f)
                    course_list.append(temp_info)
                    print(temp_info["name"], end="\t\t")
                    if len(temp_info["name"]) < 4:
                        print(end='\t')
                    print(temp_info["price"] + "\t\t" + temp_info["cycle"])
                except EOFError:
                    break

        # 输入要选择的课程，并检查所选课程是否合理。
        while True:
            select_name = input("Please input course name (quit to exit): ").strip()
            if "quit" in select_name:
                return
            for temp_course in self.course:
                if temp_course["name"] == select_name:
                    print("Selected course already exists!")
                    break
            else:
                break

        # 在当前学员课程中添加选课信息、所选课程中添加当前学员信息。
        for index, course in enumerate(course_list):
            if select_name == course["name"]:
                course_teacher = course["teachers"][0]
                if self.pay():
                    self.course.append(course)
                    course["students"].append(self.name)
                    break
                else:
                    return
        else:
            print("Selected course does not exist!")

        # 将新的课程信息写入课程文件
        with open(db_path + "courses.pkl", "wb") as f:
            for course in course_list:
                f.write(pickle.dumps(course))

        # 将新的学生信息写入学生文件
        student_list = []
        with open(db_path + "students.pkl", "rb") as f:
            while True:
                try:
                    temp_info = pickle.load(f)
                    student_list.append(self.__dict__ if temp_info["name"] == self.name else temp_info)
                except EOFError:
                    break
        with open(db_path + "students.pkl", "wb") as f:
            for temp_student in student_list:
                f.write(pickle.dumps(temp_student))

        # 将新的学生信息写入老师文件
        teacher_list = []
        with open(db_path + "teachers.pkl", "rb") as f:
            while True:
                try:
                    temp_info = pickle.load(f)
                    if temp_info["name"] == course_teacher:
                        temp_info["course"].append(select_name)
                        temp_info["students"].append(self.name)
                    teacher_list.append(temp_info)
                except EOFError:
                    break
        with open(db_path + "teachers.pkl", "wb") as f:
            for temp_student in teacher_list:
                f.write(pickle.dumps(temp_student))

    # 验证用户ID和密码才能支付
    def pay(self):
        count = 0
        while count < 3:
            count += 1
            temp_id = input("Please enter ID for payment: ")
            temp_password = input("Please enter password for payment: ")
            if temp_id == self.ID and temp_password == self.password:
                print("Successful payment!")
                return True
            else:
                print("Wrong user name or password!")
        print("User name or password entered incorrectly three times!")
        return False

    # 显示当前学生所选的所有课程
    def show_course(self):
        for course in self.course:
            print(course["name"], course["cycle"], "个月 ", course["place"], course["teachers"])

    def run(self):
        print("Student Run")
        func_menu = {
            1: "选择课程",
            2: "显示课程",
            3: "退出"
        }

        while True:
            print("学员菜单：")
            for func in func_menu:
                print(func, func_menu[func])
            order = int(input("Please input order: "))
            if order == 1:
                self.course_selection()
            if order == 2:
                self.show_course()
            if order == 3:
                return


if __name__ == '__main__':
    student = Student("1001")
    # student = Student()
    student.course_selection()
    student.show_course()
    # print(student.__dict__)
