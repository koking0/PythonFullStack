
account = {
    "is_authenticated":False,# 用户登录了就把这个改成True
    "username":"alex", # 假装这是DB里存的用户信息
    "password":"abc123" # 假装这是DB里存的用户信息
}


def login(func):
    def inner(arg1): # 再定义一层函数
        if account["is_authenticated"] is False:
            username = input("user:")
            password = input("pasword:")
            if username == account["username"] and password == account["password"]:
                print("welcome login....")
                account["is_authenticated"] = True
            else:
                print("wrong username or password!")

        if account["is_authenticated"] is True:
            func(arg1)

    return inner  # 注意这里只返回inner的内存地址，不执行


def home():
    print("---首页----")


@login
def america():
    print("----欧美专区----")

def japan():
    print("----日韩专区----")


@login
def henan(vip_level):
    if vip_level < 3:
        print("----河南专区普通会员----")
    else:
        print("欢迎来到尊贵河南口音RMB玩家私密社区".center(50,"-"))
        print("再充值500就可以获取演员微信号，幸福大门即将开启".center(50," "))

# home()
# america = login(america) # 这次执行login返回的是inner的内存地址 <function login.<locals>.inner at 0x101762840>
# henan = login(henan)  # <function login.<locals>.inner at 0x102562840>


america()  # 相当于执行inner()
henan(5)


