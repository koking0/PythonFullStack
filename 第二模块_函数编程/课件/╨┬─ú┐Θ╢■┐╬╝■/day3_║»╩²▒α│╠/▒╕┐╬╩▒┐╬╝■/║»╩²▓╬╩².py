
# def print_info(*args,**kwargs):
#     name = kwargs.get("name")
#     age = kwargs.get("age")
#     sex = kwargs.get("sex")
#     hobbie = kwargs.get("hobbie")
#     print("--------info-------")
#     print("Name:",name)
#     print("Age:",age)
#     print("Sex:",sex)
#     print("Hobbie:",hobbie if hobbie else  "大保健")
#
#
# print_info(name="Alex",age=22,sex="M")
# print_info(name="Jack",age=26,sex="M",hobbie="学习")
#
#

#
# name = "Alex Li"
#
#
# def change_name():
#     global  name
#     name = "金角大王,一个有Tesla的高级屌丝"
#     print("after change", name)
#
#
# change_name()
#
# print("在外面看看name改了么?",name)
#
# d = {"name":"Alex","age":26,"hobbie":"大保健"}
# l = ["Rebeeca","Katrina","Rachel"]
# print(id(d),id(d["name"]),id(d["age"]))
#
# def change_data(info,girls):
#     print(id(info))
#     info["hobbie"] = "学习"
#     girls.append("XiaoYun")
#
# change_data(d,l)
# print(d,l)
#



def stu_register(name,age,course,country="CN",*args,**kwargs):
    print("----注册学生信息------")
    print("姓名:",name)
    print("age:",age)
    print("国籍:",country)
    print("课程:",course)
    print(kwargs,args)

stu_register("王山炮","22","US",ss=2,country="PY",dd=2)
