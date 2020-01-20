
#
# def g_test():
#
#     while True:
#         n = yield #收到的值 给n
#
#         print("receive from outside:",n)
#
#
# g = g_test()
# g.__next__() #调用生成器，同时会发送None到yield
#
# for i in range(10):
#     g.send(i) #调用生成器，同时发送i
#

# 单线程下的多并发效果， 线程就是cpu执行的任务单元


# 吃包子 c1,c2,c3

# 生产者 ，

def consumer(name):
    print("消费才%s准备吃包子啦。。。。"% name)
    while True:
        baozi = yield  # 接收外面的包子
        print("消费者%s收到包子编号:%s"%(name,baozi))


c1 = consumer("C1")
c2 = consumer("C2")
c3 = consumer("C3")
c1.__next__()
c2.__next__()
c3.__next__()


for i in range(10):
    print("------------生成了第%s批包子----------"%i)
    c1.send(i)
    c2.send(i)
    c3.send(i)


#