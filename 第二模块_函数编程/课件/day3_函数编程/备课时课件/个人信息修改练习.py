def print_personal_info(account_dic,username):
    """
    print user info
    :param account_dic: all account's data
    :param username: username
    :return: None
    """
    person_data = account_dic[username]
    info = '''
    ------------------
    Name:   %s
    Age :   %s
    Job :   %s
    Dept:   %s
    Phone:  %s
    ------------------
    ''' %(person_data[1],
          person_data[2],
          person_data[3],
          person_data[4],
          person_data[5],
          )

    print(info)


def save_back_to_file(account_dic):
    """
    把account dic 转成字符串格式 ，写回文件
    :param account_dic:
    :return:
    """
    f.seek(0) #回到文件头
    f.truncate() #清空原文件
    for k in account_dic:
        row = ",".join(account_dic[k])
        f.write("%s\n"%row)

    f.flush()


def change_personal_info(account_dic,username):
    """
    change user info ,思路如下
    1. 把这个人的每个信息打印出来， 让其选择改哪个字段，用户选择了的数字，正好是字段的索引，这样直接 把字段找出来改掉就可以了
    2. 改完后，还要把这个新数据重新写回到account.txt，由于改完后的新数据 是dict类型，还需把dict转成字符串后，再写回硬盘

    :param account_dic: all account's data
    :param username: username
    :return: None
    """
    person_data = account_dic[username]
    print("person data:",person_data)
    column_names = ['Username','Password','Age','Job','Dept','Phone']
    for index,k in enumerate(person_data):
        #if index >1: # 0 is username and 1 is password
        print("%s.  %s: %s" %( index, column_names[index],k)  )

    choice = input("[select column id to change]:").strip()
    if choice.isdigit():
        choice = int(choice)
        if choice > 0 and choice < len(person_data): #index不能超出列表长度边界
            column_data = person_data[choice] #拿到要修改的数据
            print("current value>:",column_data)
            new_val = input("new value>:").strip()
            if new_val:#不为空
                person_data[choice] = new_val
                print(person_data)

                save_back_to_file(account_dic) #改完写回文件
            else:
                print("不能为空。。。")



account_file = "staff_list"
f = open(account_file,"r+")
raw_data = f.readlines()
accounts = {}

#把账户数据从文件里读书来，变成dict,这样后面就好查询了
for line in raw_data:
    line = line.strip()
    if not line.startswith("#"):
        items = line.split(",")
        accounts[items[0]] = items
# print(accounts)

menu = '''
1. 打印个人信息
2. 修改个人信息
3. 修改密码
'''

count = 0
while count <3:
    username = input("Username:").strip()
    password = input("Password:").strip()
    if username in accounts:
        if password == accounts[username][1]: #
            print("welcome %s ".center(50,'-') % username )
            while True: #使用户可以一直停留在这一层
                print(menu)
                user_choice = input(">>>").strip()
                if user_choice.isdigit():
                    user_choice = int(user_choice)
                    if user_choice == 1:
                        print_personal_info(accounts,username)
                    elif user_choice == 2:
                        change_personal_info(accounts,username)

                elif user_choice == 'q':
                    exit("bye.")

        else:
            print("Wrong username or password!")
    else:
        print("Username does not exist.")

    count += 1

else:
    print("Too many attempts.")