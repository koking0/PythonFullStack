

import hashlib

# md5
m = hashlib.md5()
m.update(b"Hello")
m.update(b"It's me")
print(m.digest())  # 返回2进制格式的hash值
m.update(b"It's been a long time since last time we ...")
print(m.hexdigest()) # 返回16进制格式的hash值

# sha1
s1 = hashlib.sha1()
s1.update("小猿圈".encode("utf-8"))
s1.hexdigest()

# sha256
s256 = hashlib.sha256()
s256.update("小猿圈".encode("utf-8"))
s256.hexdigest()


# sha512
s512 = hashlib.sha256()
s512.update("小猿圈".encode("utf-8"))
s512.hexdigest()

