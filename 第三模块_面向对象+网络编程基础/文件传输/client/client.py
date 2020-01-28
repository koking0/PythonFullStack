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

download_dir = r'/media/alex/新加卷/PythonProject/PythonFullStack/第三模块_面向对象&网络编程基础/文件传输/client/download'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 9902))

while True:
    # 1.向服务端发送命令
    cmd = input('>> ')
    if 'q' in cmd:
        break
    if not cmd:
        continue
    client.send(cmd.encode('utf-8'))

    # 2.接受文件内容，并写入本地
    # 2.1、首先接受报头的长度
    obj = client.recv(4)
    header_size = struct.unpack('i', obj)[0]

    # 2.2、其次接受完整的报头
    header_bytes = client.recv(header_size)

    # 2.3、然后从报头中解析真实数据的描述信息
    header_json = header_bytes.decode('utf-8')
    header_dict = json.loads(header_json)
    data_size = header_dict['data_size']
    filename = header_dict['filename']
    print(header_dict)

    # 2.4、最后接受真实的数据
    with open('%s/%s' % (download_dir, filename), 'wb') as f:
        recv_size = 0
        while recv_size < data_size:
            line = client.recv(1024)
            recv_size += len(line)
            f.write(line)

            print('已下载', str((recv_size / data_size) * 100), '%')

client.close()
