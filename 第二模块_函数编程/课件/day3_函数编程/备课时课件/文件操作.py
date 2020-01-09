

f = open(file="encode_test",mode="wb")

# s = "小猿圈".encode("utf-8")
# f.write(s)
#
# f.write("中国".encode("GBK"))

s = "小猿圈".encode("shift_jis")
print(s )
f.write(s)
f.close()