# f = open(file='/tmp/staff.txt',mode='w')
#
# f.write("Alex  CEO  600\n")
# f.write("黑姑娘  行政  5000\n")
#
# f.close()

# f = open(file='兼职白领学生空姐模特护士联系方式.txt',mode='r')
# print(f.readline())  # 读一行
# print('------分隔符-------')
# data = f.read(50)  # 读所有，剩下的所有
# f.write("haah")
# print(data)
#
# f.close()

# f = open(file='兼职白领学生空姐模特护士联系方式.txt',mode='w')
#
# f.write("黑姑娘 北京  168  48\n")  # 会追加到文件尾部
# f.close()



# f = open(file='兼职白领学生空姐模特护士联系方式.txt')
#
# for line in f:
#     line = line.split()
#     height = int(line[2])
#     weight = int(line[3])
#     if height > 170 and weight < 50:
#         print(line)


# for i in range(100):
#     print(i)

# f = open('兼职白领学生空姐模特护士联系方式.txt',"a")
#
# f.seek(10)
# print(f.tell())
# f.truncate()

# w+
# f = open("write_and_read","w+")
# f.write("hello world1\n")
# f.write("hello world2\n")
# f.write("hello world3\n")
# f.write("hello world4\n")
# f.write("hello world5\n")
# f.seek(0)
# print(f.readline())

# #r+ a+
# f = open("write_and_read","a+")
# f.write("hello1\n")
# f.write("hello2\n")
#
# f.seek(0)
# print(f.readline())

# import os
#
# # 不占内存修改文件
# old_file= '兼职白领学生空姐模特护士联系方式.txt'
# new_file = '兼职白领学生空姐模特护士联系方式.txt.new'
# f = open(old_file,"r")
# f_new = open(new_file,"w")
#
# old_str = "深圳"
# new_str = "广州"
#
# for line in f:
#     if "深圳" in line:
#         line = line.replace(old_str,new_str)
#     f_new.write(line)
#
# f.close()
# f_new.close()
#
# os.rename(new_file,old_file)


f = open("stock_data")
for line in f:
    line = line.split()
    print(line)