

# import pickle
data = {'k1':123,'k2':'Hello'}
#
# # pickle.dumps 将数据通过特殊的形式转换位只有python语言认识的字符串
# p_str = pickle.dumps(data)  # 注意dumps会把数据变成bytes格式
# print(p_str)
#
# # pickle.dump 将数据通过特殊的形式转换位只有python语言认识的字符串，并写入文件
# with open('result.pk',"wb") as fp:
#     pickle.dump(data,fp)

import json
# json.dumps 将数据通过特殊的形式转换位所有程序语言都认识的字符串
j_str = json.dumps(data) # 注意json dumps生成的是字符串，不是bytes
print(j_str)

#dump入文件
with open('result.json','w') as fp:
    json.dump(data,fp)

#从文件里load
with open("result.json") as f:
    d = json.load(f)
    print(d)

#
# import pickle
# pickle.load
# f = open("result.pk","rb")
# d = pickle.load(f)
# print(d)