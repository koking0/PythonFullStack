

def outer():
    name = 'alex'

    def inner():
        print("在inner里打印外层函数的变量",name)

    return inner # 注意这里只是返回inner的内存地址，并未执行


f = outer() # <function outer.<locals>.inner at 0x1027621e0>

f()  # 相当于执行的是inner(), 注意此时outer已经执行完毕，正常情况下outer里的内存都已经释放了，但此时由于闭包的存在，我们却还可以
