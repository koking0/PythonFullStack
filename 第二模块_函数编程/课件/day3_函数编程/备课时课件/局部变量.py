

l = ["Rebeeca","Katrina","Rachel"]
n = 2
def change():
    n = 3
    print(id(n),n)
    print(locals())

print(id(n),globals())
change()
print(n)