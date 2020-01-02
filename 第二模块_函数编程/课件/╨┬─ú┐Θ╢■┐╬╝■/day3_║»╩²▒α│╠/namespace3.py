
level = 'L0'
#n = 22
#dir = 333333

def func():
    level = 'L1'
    #n = 33
    print(locals())

    def outer():
        #n = 44
        level = 'L2'
        print("outer:",locals(),dir)

        def inner():
            #n = 55
            level = 'L3'
            print("inner:",locals(),dir) #此处打印的n是多少？
        inner()
    outer()


func()