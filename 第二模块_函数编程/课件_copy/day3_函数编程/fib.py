# 0 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
#
# a = 0
# b = 1
#
#
# a = 1 # a= b
# b = 1 # a + b
#
# a = 1
# b = 2
#
# a = 2
# b = 3


def fib(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        tmp = a # 给新的a赋值前先把旧值存下来
        a = b  # 新的a=1
        b = tmp + b
        #print(b)
        yield b # 暂停 return
        count += 1


f= fib(20)
print(next(f))
print(next(f))
print("------do sth else....")
print(f.__next__())
print(next(f))
print(next(f))
print(next(f))
print(next(f))