
#
# names = ["alex","rain","jack"]
#
# f = open("eval_test","w")
# f.write(str(names) )


f = open("eval_test")

d = eval(f.read())


print(type(d))

print(d[2])