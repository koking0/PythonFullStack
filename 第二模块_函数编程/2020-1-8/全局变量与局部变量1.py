name = "Alex"


def change():
    name = "Coco"
    age = 19
    print(locals())     # 打印所有的局部变量
    print(globals())    # 打印所有的全局变量
    print(name, id(name))


change()
print(name, id(name))
