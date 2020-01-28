#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/22 下午3:46
# @File     : client.py
# @Project  : PythonFullStack
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import json
import socket
import struct

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(('127.0.0.1', 9900))

while True:
    # 1.向服务端发送命令
    cmd = input('>> ')
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))

    # 2.接受命令的结果并打印
    # 2.1、首先接受报头的长度
    obj = client.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 2.2、其次接受完整的报头
    header_bytes = client.recv(header_size)

    # 2.3、然后从报头中解析真实数据的描述信息
    header_json = header_bytes.decode('utf-8')
    header_dict = json.loads(header_json)
    data_size = header_dict['data_size']
    print(header_dict)

    # 2.4、最后接受真实的数据
    recv_size = 0
    recv_data = b''
    while recv_size < data_size:
        res = client.recv(1024)
        recv_data += res
        recv_size += len(res)

    print(recv_data.decode('utf-8'))
