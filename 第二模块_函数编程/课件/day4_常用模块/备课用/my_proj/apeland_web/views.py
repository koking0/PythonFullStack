import sys ,os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #__file__的是打印当前被执行的模块.py文件相对路径，注意是相对路径
# print(BASE_DIR) # 输出是/Users/alex/PycharmProjects/apeland_py_learn/day4_常用模块/my_proj
#
# sys.path.append(BASE_DIR)

from  my_proj import settings

def sayhi():
    print('hello world!')

print("views-----",settings.DATABASES)





