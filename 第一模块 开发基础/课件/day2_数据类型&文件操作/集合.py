




s_1024 = {"佩奇","老男孩","海峰","马JJ","老村长","黑姑娘","Alex"}

s_pornhub = {"Alex","Egon","Rain","马JJ","Nick","Jack"}

print(s_1024 & s_pornhub) # 交集, elements in both set

print(s_1024 | s_pornhub)  # 并集 or 合集

print(s_1024 - s_pornhub)  # 差集 , only in 1024
print(s_pornhub - s_1024)  # 差集,  only in pornhub

print(s_1024 ^ s_pornhub)  # 对称差集, 把脚踩2只船的人T出去

print(s_1024.isdisjoint(s_pornhub))     # 判断2个集合是不是不相交，返回True or False
print(s_1024.issubset(s_pornhub))       # 判断s_1024是不是s_pornhub的子集，返回True or False
print(s_1024.issuperset(s_pornhub))     # 判断s_1024是不是s_pornhub的父集，返回True or False

