#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/27 22:33
# @File     : main.py
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
import hashlib
import configparser
import subprocess

from conf import settings


class FTPServer:
    """处理与客户端所有的socket server"""

    MSG_SIZE = 1024
    STATUS_CODE = {
        200: "Passed authentication!",
        201: "Wrong username or password!",
        202: "User is not exited!",
        300: "File exited!",
        301: "File not exited!",
        302: "Message size!"
    }

    def __init__(self, management_instance):
        self.management_instance = management_instance
        self.accounts = self.load_accounts()
        self.current_dir = None
        self.user_obj = None

        # 声明socket实例
        self.request, self.addr = None, None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((settings.HOST, settings.PORT))
        self.sock.listen(settings.MAX_SOCKET_LISTEN)

    def run_forever(self):
        """启动socket server"""
        print("starting FTP server on %s:%s".center(50, "-") % (settings.HOST, settings.PORT))

        while True:
            # 开始监听
            self.request, self.addr = self.sock.accept()
            print("got a new connection from %s..." % (self.addr,))
            self.handle()

    def handle(self):
        """处理与用户的所有指令交互"""

        while True:
            raw_data = self.request.recv(self.MSG_SIZE)
            print("------->", raw_data)

            if not raw_data:
                print("Connection %s is lost..." % (self.addr,))
                del self.request, self.addr
                break

            data = json.loads(raw_data.decode("utf-8"))
            action_type = data.get("action_type")
            if action_type:
                if hasattr(self, "_%s" % action_type):
                    func = getattr(self, "_%s" % action_type)
                    func(data)
            else:
                print("invalid command.")

    def _ls(self, data):
        """run dir command and send result to client"""
        print(self.current_dir)
        cmd_obj = subprocess.Popen("dir %s" % self.current_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout = cmd_obj.stdout.read()
        stderr = cmd_obj.stderr.read()
        cmd_result = stdout + stderr

        if not cmd_result:
            cmd_result = b"Current dir has no file at all."

        self.send_response(302, cmd_result_size=len(cmd_result))
        self.request.sendall(cmd_result)

    def _get(self, data):
        """client download files through this method"""
        # 1.拿到文件名
        filename = data.get("filename")
        filepath = os.path.join(self.user_obj["home"], filename)

        # 2.判断文件是否存在
        # 2.1、如果存在，返回状态码+文件大小
        if os.path.isfile(filepath):
            file_size = os.stat(filepath).st_size
            self.send_response(300, file_size=file_size)
            print("Ready to send file")

            # 发送客户端请求的文件
            with open(filepath, "rb") as file:
                for line in file:
                    self.request.send(line)
                else:
                    print("[%s] send done..." % filename)

        # 2.2、如果不存在，返回状态码
        else:
            self.send_response(301)
            print(self.STATUS_CODE.get(301))

    def _auth(self, data):
        """处理用户认证请求"""
        if self.authenticate(data.get("username"), data.get("password")):
            self.send_response(status_code=200)
        else:
            self.send_response(status_code=201)

    def authenticate(self, username, password):
        """用户认证方法"""
        if username in self.accounts:
            _password = self.accounts[username]["password"]
            md5 = hashlib.md5()
            md5.update(password.encode("utf-8"))
            md5_password = md5.hexdigest()
            print("password: ", password)
            print("_password: ", _password)
            print("md5_password: ", md5_password)
            if md5_password == _password:
                print("Password authentication...")
                # set user obj
                self.user_obj = self.accounts[username]
                # set user home directory
                self.user_obj["home"] = os.path.join(settings.USER_HOME_DIR, username)
                # set current directory
                self.current_dir = self.user_obj["home"]
                return True
            else:
                print("Wrong username or password...")
                return False
        else:
            print("User is not exited...")
            return False

    @staticmethod
    def load_accounts():
        """加载所有账号信息"""
        config_obj = configparser.ConfigParser()
        config_obj.read(settings.ACCOUNT_FILE)

        print(config_obj.sections())
        return config_obj

    def send_response(self, status_code, *args, **kwargs):
        """
        打包发送消息给客户端
        :param status_code:
        :param args:
        :param kwargs:
        :return:
        """
        data = kwargs
        data["fill"] = ""
        data["status_code"] = status_code
        data["status_msg"] = self.STATUS_CODE[status_code]

        bytes_data = json.dumps(data).encode("utf-8")

        if len(bytes_data) < self.MSG_SIZE:
            data["fill"] = data["fill"].zfill(self.MSG_SIZE - len(bytes_data))
            bytes_data = json.dumps(data).encode("utf-8")

        self.request.send(bytes_data)
