

# 100/2 = 50
# 50/2 = 25

# n = 100
#
# while n > 0 :
#     n = int(n / 2 )
#     print(n )
#


def calc(n):

    print(n )
    n = int(n /2) # 50
    if n > 0:
        calc(n) # 50

    print(n)

