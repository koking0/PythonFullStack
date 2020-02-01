#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/27 22:33
# @File     : interactive.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import os
import json
import shutil
import time
import socket
import hashlib
import subprocess
import configparser

from conf import settings


class FTPServer:
    """处理与客户端所有的socket server"""

    MSG_SIZE = 1024
    STATUS_CODE = {
        700: "Pass password verification.",         # 用户密码验证通过
        701: "User name does not exist.",           # 用户名不存在
        702: "Password error",                      # 密码错误
        710: "File exists.",                        # 客户端请求下载文件时，服务端存在此文件
        711: "File does not exist.",                # 客户端请求下载文件时，服务端不存在此文件
        712: "File size and MD5 values.",           # 客户端请求下载文件时，如果服务端存在此文件，先返回文件大小和MD5值
        713: "Resend file size and MD5 value.",     # 客户端请求重新下载文件时，如果服务端还存在此文件，返回文件大小和MD5值
        714: "MD5 value not match.",                # 客户端请求重新下载文件时，文件MD5值不一致
        720: "Catalog changed.",                    # 客户端请求更改目录时，如果目录存在，返回目录更改成功
        721: "Directory does not exist.",           # 客户端请求更改目录时，如果目录不存在，返回给用户目录不存在
        722: "Beyond access",                       # 客户端请求更改的目录超出访问权限
        730: "Folder created successfully.",    # 文件夹创建成功
        731: "Folder already exists.",          # 文件夹已存在
        740: "Replication success.",                # 文件或文件夹复制成功
        741: "Original file does not exist",        # 原文件不存在
        742: "Target file already exists",          # 目标文件已存在
        743: "Path exceeds access rights",          # 路径超出访问权限
        760: "Message size",                        # 消息的大小
        770: "Remove file or folder successfully."  # 删除文件或文件夹成功
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
            try:
                self.handle()
            except Exception as exception:
                self.request.close()
                print(exception)
                print("Error happen with client, close connection")

    def handle(self):
        """处理与用户的所有指令交互"""
        while True:
            raw_data = self.request.recv(self.MSG_SIZE)

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

    def _auth(self, data):
        """用户认证方法"""
        username = data.get("username")
        if username in self.accounts:
            md5 = hashlib.md5()
            md5.update(data.get("password").encode("utf-8"))
            md5_password = md5.hexdigest()
            ini_password = self.accounts[username]["password"]
            if md5_password == ini_password:
                # set user obj
                self.user_obj = self.accounts[username]
                # set user home directory
                self.current_dir = self.user_obj["home"] = os.path.join(settings.USER_HOME_DIR, username)
                self.send_response(status_code=700)
            else:
                self.send_response(status_code=702)
        else:
            self.send_response(status_code=701)

    def _ls(self, data):
        """run dir command and send result to client"""
        cmd = subprocess.Popen("dir %s" % self.current_dir, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = cmd.stdout.read(), cmd.stderr.read()
        result = stdout + stderr if stdout + stderr else b"Current dir has no file at all."
        self.send_response(760, result_size=len(result))
        self.request.sendall(result)

    def _cd(self, data):
        """根据用户的target_dir改变self.user_current_dir的值"""
        target_path = os.path.abspath(os.path.join(self.current_dir, data.get("target_dir")))

        if os.path.isdir(target_path):
            if target_path.startswith(self.user_obj["home"]):
                self.current_dir = target_path
                client_current_dir = self.current_dir.replace(self.user_obj['home'], "")
                self.send_response(720, current_dir=client_current_dir)
            else:
                self.send_response(722)
        else:
            self.send_response(721)

    def _cp(self, data):
        """复制文件或文件夹"""
        original_path = os.path.abspath(os.path.join(self.current_dir, data.get("original_path")))
        target_path = os.path.abspath(os.path.join(self.current_dir, data.get("target_path")))
        if os.path.isfile(original_path) or os.path.isdir(original_path):
            if original_path.startswith(self.user_obj["home"]) or target_path.startswith(self.user_obj["home"]):
                if os.path.isfile(target_path) or os.path.isdir(target_path):
                    self.send_response(742)
                else:
                    shutil.copy(original_path, target_path)
                    self.send_response(740)
            else:
                self.send_response(743)
        else:
            self.send_response(741)

    def _mv(self, data):
        """移动文件或文件夹"""
        original_path = os.path.abspath(os.path.join(self.current_dir, data.get("original_path")))
        target_path = os.path.abspath(os.path.join(self.current_dir, data.get("target_path")))
        if os.path.isfile(original_path) or os.path.isdir(original_path):
            if original_path.startswith(self.user_obj["home"]) or target_path.startswith(self.user_obj["home"]):
                if os.path.isfile(target_path):
                    self.send_response(742)
                else:
                    shutil.move(original_path, target_path)
                    self.send_response(740)
            else:
                self.send_response(743)
        else:
            self.send_response(741)

    def _rm(self, data):
        """删除文件或文件夹"""
        target_path = os.path.abspath(os.path.join(self.current_dir, data.get("target_path")))
        if os.path.isfile(target_path):
            os.remove(target_path)
            self.send_response(770)
        elif os.path.isdir(target_path):
            os.rmdir(target_path)
            self.send_response(770)
        else:
            self.send_response(741)

    def _mkdir(self, data):
        """创建文件夹"""
        target_path = os.path.abspath(os.path.join(self.current_dir, data.get("target_path")))
        if os.path.isdir(target_path):
            self.send_response(731)
        else:
            os.mkdir(target_path)
            self.send_response(730)

    def _get(self, data):
        """client download files through this method"""
        # 1.拿到文件名
        filename = data.get("filename")
        filepath = os.path.join(self.current_dir, filename)
        # 2.判断文件是否存在
        # 2.1、如果存在，返回状态码+文件大小
        if os.path.isfile(filepath):
            # 发送客户端请求的文件
            with open(filepath, "rb") as file:
                data = file.read()
            md5 = hashlib.md5()
            md5.update(data)
            self.send_response(712, file_size=os.path.getsize(filepath), file_md5=md5.hexdigest())
            self.request.sendall(data)
            print("[%s] send done..." % filename)
        else:
            # 2.2、如果不存在，返回状态码
            self.send_response(711)

    def _put(self, data):
        """client uploads file to server"""
        local_file, full_path, received_size, total_size = \
            data.get("file_name"), os.path.join(self.current_dir, data.get("file_name")), 0, data.get("file_size")
        filename = "%s.%s.%s" % (self.current_dir, time.time(), local_file) if os.path.isfile(full_path) else full_path
        with open(filename, "wb") as file:
            while received_size < total_size:
                data = self.request.recv(total_size - received_size if total_size - received_size < 8192 else 8192)
                received_size += len(data)
                file.write(data)
            else:
                print("File %s recv done." % local_file)

    def _re_get(self, data):
        """resend unfinished file on client"""
        # 1.提取文件路径
        full_path = os.path.join(self.user_obj["home"] + data.get("file_path"), data.get("filename"))
        # 2.判断文件是否存在，
        if os.path.isfile(full_path):
            # 2.1、文件存在，判断文件大小是否与客户端发过来的一致
            with open(full_path, "rb") as file:
                file_data = file.read()
            md5 = hashlib.md5()
            md5.update(file_data)
            if md5.hexdigest() == data.get("file_md5"):
                # 2.1.1、如果一致，准备续传，并seek到指定位置循环发送
                self.send_response(713, file_size=os.path.getsize(full_path) - data.get("recv_size"))
                with open(full_path, "rb") as file:
                    file.seek(data.get("recv_size"))
                    for line in file:
                        self.request.send(line)
                    else:
                        print("File resend done!".center(50, "-"))
            else:
                self.send_response(714)
        else:
            # 2.2、文件不存在，返回状态码和错误信息
            self.send_response(711)

    def send_response(self, status_code, **kwargs):
        """打包发送消息给客户端"""
        data = {
            "status_code": status_code,
            "status_msg": self.STATUS_CODE[status_code],
            "fill": ""
        }
        data.update(kwargs)
        bytes_data = json.dumps(data).encode("utf-8")
        if len(bytes_data) < self.MSG_SIZE:
            data["fill"] = data["fill"].zfill(self.MSG_SIZE - len(bytes_data))
            bytes_data = json.dumps(data).encode("utf-8")
        self.request.send(bytes_data)

    @staticmethod
    def load_accounts():
        """加载所有账号信息"""
        config_obj = configparser.ConfigParser()
        config_obj.read(settings.ACCOUNT_FILE)
        return config_obj
