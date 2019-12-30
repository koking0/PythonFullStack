import re

f = open("兼职模特空姐联系方式.txt")

phone_list = re.search( "[0-9]{11}", f.read() )

print(phone_list)
# phone_list = [ ]
#
# for line in f:
#     name,region,height,weight,phone = line.split()
#     if phone.startswith("1"):
#         phone_list.append(phone)
#
#
# print(phone_list)