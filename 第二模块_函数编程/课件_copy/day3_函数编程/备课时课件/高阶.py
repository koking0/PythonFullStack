



def get_abs(n):
    if n < 0 :
        n = int(str(n).strip("-"))
    return n

def add(x,y,f):
    return f(x) + f(y)


res = add(3,-6,get_abs)

print(res)