

def outer():
    name = "小猿圈，自学编程"

    def inner():
        print("Inner",name)

    return inner


func = outer()  # 返回的是inner的内存地址， inner

func() #inner()

