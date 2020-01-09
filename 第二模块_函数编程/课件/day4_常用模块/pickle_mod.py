import pickle

d = {
    "name":"alex",
    "role": "police",
    "blood": 76,
    "weapon": "AK47"
}

alive_players = ["alex","jack","rain"]


import datetime

print(pickle.dumps(datetime.datetime.now()))

# d_dump= pickle.dumps(d) # 序列化
# print(pickle.loads(d_dump)) #反序列化
#
# f = open("game.pkl","wb")
# #f.write(d_dump)
# pickle.dump(d,f) #First in first out FIFO #First in last out
# pickle.dump(alive_players,f)

# dump 写入文件
# dumps 生成序列化的字符串
#
# load 从文件加载
# loads 把序列化的字符串反向解析