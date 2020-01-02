

import time


print(time.time())
print(time.localtime())
t1 = time.gmtime()

print(time.mktime(t1))

#time.sleep(3)
print("------")
print(time.asctime())
print(time.ctime(1233333))

print(time.strftime("%Y.%m-%d %H:%M %p %j %z",time.localtime()))

print(time.strptime("2020/04/01 9:30 ", "%Y/%m/%d %I:%M "))