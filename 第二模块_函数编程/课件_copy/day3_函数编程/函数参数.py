
#
# def calculate(x,y,z):
#
#     res = x**y
#     print(z)
# n = calculate(5,8,9)
# print(n)

# def register(name,age,major="CS",country="CN"):
#     """
#     学籍注册程序
#     :param name: str
#     :param age:  integer
#     :param major: str  ,Chinese, CS
#     :param country: JP,CN,US
#     :return:
#     """
#     info = """
#     --------- 你的注册信息 ----------
#     name: %s
#     age : %s
#     major: %s
#     country: %s
#     """ %(name,age,major,country)
#     print(info)
#
#
# register(22,"alex")
# register("李四",26,"Math")
# register("Mack",22,"CS","US")


# def register(name,age,major="CS",country="CN",*args,**kwargs):
#     """
#     学籍注册程序
#     :param name: str
#     :param age:  integer
#     :param major: str  ,Chinese, CS
#     :param country: JP,CN,US
#     :return:
#     """
#     info = """
#     --------- 你的注册信息 ----------
#     name: %s
#     age : %s
#     major: %s
#     country: %s
#     """ %(name,age,major,country)
#     print(info)
#     print(args,kwargs.get("addr"))

# register("alex","ddddd",major="中文",age="22",sex="M",phone=13651054608)
# register("alex",major="中文",age="22",sex="M",addr="昌平沙河")


locals()

def register(name,*args,**kwargs):
    print(name,args,kwargs)


register("Alex",22,"Math",sex="M")