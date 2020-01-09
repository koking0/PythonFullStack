

import re

f = open("兼职模特空姐联系方式.txt")
data = f.read()

print(re.findall("[0-9]{11}",data))


