'''
作业：双色球选购
1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
2 确保用户不能重复选择，不能超出范围
3 用户输入有误时有相应的错误提示
4 最后展示用户选择的双色球的号码
效果图：双色球作业展示
升级需求：
1 一个while循环


思路：

1.用列表choose记录选择的球

2.while循环更新falg的值

3.while循环中：
    提示用户选择；
    判断选择是否超出范围；
    判断选择是否重复；
    判断选择是否完成
'''

red_choose = []
blue_choose = []

while True:
    if len(red_choose) != 6:
        print("\nPlease choose red ball ", len(red_choose) + 1, end='')
        temp = int(input(" (The red ball range is 1-32) "))
        if temp < 1 or temp > 32:
            print("Please choose red ball in range 1 - 32")
        elif temp in red_choose:
            print("red ball ", temp, " is been chosen")
        else:
            red_choose.append(temp)
        continue

    if len(blue_choose) != 2:
        print("\nPlease choose blue ball ", len(blue_choose) + 1, end='')
        temp = int(input(" (The blue ball range is 1-16) "))
        if temp < 1 or temp > 16:
            print("Please choose blue ball in range 1 - 16")
        elif temp in blue_choose:
            print("blue ball ", temp, " is been chosen")
        else:
            blue_choose.append(temp)

    if len(blue_choose) == 2 and len(red_choose) == 6:
        break

print("\n\nYour Chosen:")
red_choose.sort()
blue_choose.sort()
print("red ball: ", red_choose)
print("blue ball: ", blue_choose)

'''
缺点：
    1.红蓝重复操作，可以写成一个函数
    2.存在bug，如果不输入数字直接回车会报错，可以用try,catch捕获
'''