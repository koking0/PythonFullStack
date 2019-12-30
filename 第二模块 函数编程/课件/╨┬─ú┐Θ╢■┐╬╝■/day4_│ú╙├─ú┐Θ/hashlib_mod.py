
import hashlib

m = hashlib.md5()
m.update(b"hello alex")
print(m.hexdigest())
m.update("欢迎来到小猿圈".encode("utf-8"))

#print(m.digest()) # 消化b
print(m.hexdigest())


m2 = hashlib.md5()
m2.update("hello alex欢迎来到小猿圈".encode("utf-8"))
print(m2.hexdigest())


alipay  hello alex a3e3bb5d7611493a6a1200af508fbc0f alipay
jd      hello alex a3e3bb5d7611493a6a1200af508fbc0f   a3e3bsssfb5d76114sdfsdfs93a6a1200af508fbc0f
weixin  hello alex a3e3bb5d7611493a6a1200af508fbc0f

撞库 穷举
脱库
加盐 aldfsf

alex  -->md5 a3e3bb5d7611493a6a1200a2324234234
hello alex -->md5 a3e3bb5d7611493a6a1200af508fbc0f


