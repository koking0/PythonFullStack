
# f = open(file='D:/工作日常/staff.txt',mode='w')
#
# f.write("Alex  CEO  600\n")
# f.write("黑姑娘  行政  5000\n")
#
# f.close()

# f = open(file='兼职白领学生空姐模特护士联系方式.txt',mode='r')
# print(f.readline())  # 读一行
# print('------分隔符-------')
# data = f.read()  # 读所有，剩下的所有
#
# print(data)
#
# f.close()

# f = open(file='兼职白领学生空姐模特护士联系方式.txt',mode='r')
#
# for line in f:
#     line = line.split()
#     name,addr,height,weight,phone = line
#     height = int(height)
#     weight = int(weight)
#     if height > 170 and weight <= 50:
#         print(line)
#
# f.write()
# f.close()


f = open(file='兼职白领学生空姐模特护士联系方式.txt', mode='r+')

f.write("{小猿圈}")  # 默认写在第一行，会覆盖原有数据
f.seek(50)          # 想改中间的数据，就得seek到对应位置
f.write("{黑姑娘}")
f.close()
