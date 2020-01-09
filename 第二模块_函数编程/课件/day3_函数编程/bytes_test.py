

f = open("bytes.txt","r")

#f.write("你好未来")
# f.write("\n你好未来2".encode("gbk"))
# f.write("\n你好未来2".encode("utf-8"))

print(f.read())
f.close()