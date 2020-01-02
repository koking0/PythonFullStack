
account = {
    "is_authenticated":False,# 用户登录了就把这个改成True
    "username":"alex", # 假装这是DB里存的用户信息
    "password":"abc123" # 假装这是DB里存的用户信息
}


def login(func):
    if account["is_authenticated"] is False:
        username = input("user:")
        password = input("pasword:")
        if username == account["username"] and password == account["password"]:
            print("welcome login....")
            account["is_authenticated"] = True
        else:
            print("wrong username or password!")

    if account["is_authenticated"] is True:
        func()


def home():
    print("---首页----")


def america():
    print("----欧美专区----")


def japan():
    print("----日韩专区----")


def henan():
    print("----河南专区----")


home()
america = login(america)
henan  = login(henan)

#america()


