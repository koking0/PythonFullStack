

#
# n = 100
# while n > 0:
#     n = int(n/2)
#     print(n)
#


# def calc(n):
#
#     n = int(n/2)
#     print(n)
#     if n > 0:
#         calc(n)
#
# calc(100)

def calc(n):

    n = int(n/2)
    print(n)
    if n > 0:
         calc(n)
    print(n)


calc(10)

