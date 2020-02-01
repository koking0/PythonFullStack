#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/27 22:55
# @File     : management.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# 参数处理模块
import hashlib
import configparser

from conf import settings
from core import interactive


class ManagementTool:
    """负责对运行服务端输入的指令进行解析并调用相应的模块处理"""

    def __init__(self, sys_argv):
        self.sys_argv = sys_argv
        self.verify_argv()

    def verify_argv(self):
        """验证指令合法"""
        if len(self.sys_argv) < 2:
            self.help_msg()

        cmd = self.sys_argv[1]
        if not hasattr(self, cmd):
            print("invalid argument")
            self.help_msg()

    def execute(self):
        """解析并执行指令"""
        cmd = self.sys_argv[1]
        func = getattr(self, cmd)
        func()

    def start(self):
        """start ftp server"""
        server = interactive.FTPServer(self)
        server.run_forever()

    @staticmethod
    def creat_user():
        """创建用户"""
        md5 = hashlib.md5()
        nickname = input("Please input user nickname: ").strip()

        config_obj = configparser.ConfigParser()
        config_obj.read(settings.ACCOUNT_FILE)
        if nickname in config_obj.sections():
            exit("User already exited!")

        md5.update(input("Please input user password: ").strip().encode("utf-8"))
        user_space = input("Please input user total space: ").strip()
        password = md5.hexdigest()

        config_obj.add_section(nickname)
        config_obj.set(nickname, "name", nickname)
        config_obj.set(nickname, "password", password)
        config_obj.set(nickname, "total_space", user_space)
        config_obj.set(nickname, "used_space", "0")
        config_obj.write(open(settings.ACCOUNT_FILE, "w+"))

    @staticmethod
    def help_msg():
        msg = """
        -------start           start FTP server-------
        -------creat_user      creat a FTP user-------
        """
        exit(msg)
