# staff_list = [
#     ["Alex",23,"CEO",66000],
#     ["黑姑娘",24,"行政",4000],
#     ["佩奇",26,"讲师",40000],
#     # [xxx,xx,xx,xxx]
#     # [xxx,xx,xx,xxx]
#     # [xxx,xx,xx,xxx]
# ]
#
# for i in staff_list:
#     if i[0] == '黑姑娘':
#         print(i)
#

info = {
    "name":"小猿圈",
    "mission": "帮一千万极客高效学编程",
    "website": "http://apeland.com"
}

for k in info:
    print(k,info[k])

names = {
    "alex": [23, "CEO", 66000],
    "黑姑娘": [24, "行政", 4000],
}

names["佩奇"] = [26, "讲师", 40000]
names.setdefault("oldboy",[50,"boss",100000])  # D.setdefault(k[,d]) -> D.get(k,d), also set D[k]=d if k not in D

#
# names.pop("alex") # 删除指定key
# names.popitem()   # 随便删除1个key
# del names["oldboy"] # 删除指定key,同pop方法
# names.clear()     # 清空dict
#
# print(names)
