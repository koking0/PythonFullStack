# name = "小猿圈"
#
#
# def change():
#     #name = "小猿圈，自学编程"
#
#     def change2():
#         # global name  如果声明了这句，下面的name改的是最外层的全局变层
#         #name = "小猿圈，自学编程不要钱" #这句注释掉的话，下面name打印的是哪个值？
#         print("第3层打印", name)
#
#     change2()  # 调用内层函数
#     print("第2层打印", name)
#
#
# change()
#
# print("最外层打印", name)


# #这段代码
# def calc(x,y):
#     return x**y
#
# print(calc(2,5))
#
# c = lambda x,y:x**y

# print(c(2,8))

def calc(x):
    return x**2

#res = map(calc, [1,5,7,4,8])
res = map(lambda x:x**2 if x >10 else x**3, [1,5,7,4,8,12])

print(res )
for i in res :
    print(i )