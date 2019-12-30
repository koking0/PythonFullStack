"""
作业：双色球选购
1 双色球（假设一共八个球，6个红球，球号1-32、2个蓝球，球号1-16）
2 确保用户不能重复选择，不能超出范围
3 用户输入有误时有相应的错误提示
4 最后展示用户选择的双色球的号码
效果图：双色球作业展示
升级需求：
1 一个while循环
"""
count = 1
red_list = []
blue_list = []
while count <= 8:
    if count <= 6:
        red_ball = int(input("[%d]select red ball:" % count))   # 这里的%count不用加括号
        if red_ball < 1 or red_ball > 32:
            print("only can select between 1-32")
        elif red_ball in red_list:
            print("number " + str(red_ball) + " is already exist in red ball list")
        else:
            red_list.append(red_ball)
            count += 1
    else:
        blue_ball = int(input("[%d]select blue ball:" % (count - 6)))
        if blue_ball < 1 or blue_ball > 16:
            print("only can select between 1-16")
        elif blue_ball in blue_list:
            print("number " + str(blue_ball) + " is already exist in red ball list")
        else:
            blue_list.append(blue_ball)
            count += 1
print("Red_ball:", red_list)
print("Red_ball:", blue_list)
print("Good Luck.")
