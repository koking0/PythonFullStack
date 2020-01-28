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
import os
import socket
import struct

share_dir = r'/media/alex/新加卷/PythonProject/PythonFullStack/第三模块_面向对象&网络编程基础/文件传输/server/share'


def get_order(connect, filename):
    # 3.把命令的结果返回给客户端
    # 3.1、首先制作固定长度的报头
    header_dict = {
        'filename': filename,
        'data_size': os.path.getsize('%s/%s' % (share_dir, filename))
    }
    header_json = json.dumps(header_dict)
    header_bytes = header_json.encode('utf-8')

    # 3.2、其次把报头长度发送给客户端
    connect.send(struct.pack('i', len(header_bytes)))

    # 3.3、然后发送报头数据
    connect.send(header_bytes)

    # 3.3、最后再发送文件的数据
    with open('%s/%s' % (share_dir, filename), 'rb') as f:
        for line in f:
            connect.send(line)


def run():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 9902))
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

                # 2.解析命令，拿到命令参数
                cmds = cmd.decode('utf-8').split()
                order = cmds[0]
                filename = cmds[1]
                if order == 'get':
                    get_order(connect, filename)
            except ConnectionResetError:
                break
        connect.close()


if __name__ == '__main__':
    run()
