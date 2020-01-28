#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/22 下午3:46
# @File     : server.py
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
import subprocess

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(('127.0.0.1', 9900))
server.listen(5)

print('Starting...')
while True:  # 链接循环
    connect, client_address = server.accept()
    print(client_address)

    while True:  # 通信循环
        try:
            # 1.接收命令
            cmd = connect.recv(1024)
            if not cmd:
                break
            print('recv commend: ', cmd)

            # 2.执行命令，拿到命令执行结果
            obj = subprocess.Popen(cmd.decode('utf-8'), shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
            stdout = obj.stdout.read()
            stderr = obj.stderr.read()

            # 3.把命令的结果返回给客户端
            # 3.1、首先制作固定长度的报头
            header_dict = {
                'filename': 'filename',
                'data_size': len(stdout) + len(stderr)
            }
            header_json = json.dumps(header_dict)
            header_bytes = header_json.encode('utf-8')

            # 3.2、其次把报头长度发送给客户端
            connect.send(struct.pack('i', len(header_bytes)))

            # 3.3、然后发送报头数据
            connect.send(header_bytes)

            # 3.3、最后再发送真实的数据
            connect.send(stdout)
            connect.send(stderr)
        except ConnectionResetError:
            break
    connect.close()
