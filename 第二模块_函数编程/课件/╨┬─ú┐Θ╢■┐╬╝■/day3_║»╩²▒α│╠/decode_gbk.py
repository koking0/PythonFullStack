
f = open("win_data.txt","rb")
s = f.read()
f.close()


s_unicode = s.decode("gbk") #转成unicode

s_utf8 = s_unicode.encode("utf-8") #编码成utf-8

f = open("win_data.txt","wb")
f.write(s_utf8)
f.close()


# 2进制模式rb wb ab
# r 文本模式 ， 把2进制解码成str , unicode