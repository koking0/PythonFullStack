


def fib(max):
    a,b = 0,1
    n = 0  # 斐波那契数
    while n < max:
        n = a + b
        a = b # 把b的旧值给到a
        b = n # 新的b = a + b(旧b的值)
        #print(n)
        yield n # 程序走到这，就会暂停下来，返回n到函数外面，直到被next方法调用时唤醒

f = fib(100) # 注意这句调用时，函数并不会执行，只有下一次调用next时，函数才会真正执行




# print(f)
#print(f.__next__(),'333')

for i in f:
    print(i)
# print(f.__next__())
# print("干点别的事")
# print(f.__next__())
# print(f.__next__())
