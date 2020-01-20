

def get_abs(n):
    return int(str(n).strip("-"))


def add(x,y,f):

    return f(x) + f(y)

print(add(5,-10,get_abs))