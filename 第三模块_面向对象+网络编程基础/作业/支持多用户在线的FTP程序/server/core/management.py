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
from core import main


class ManagementTool:
    """负责对用户输入的指令进行解析并调用相应的模块处理"""

    def __init__(self, sys_argv):
        self.sys_argv = sys_argv
        self.verify_argv()
        print(self.sys_argv)

    def verify_argv(self):
        """验证指令合法"""
        if len(self.sys_argv) < 2:
            self.help_msg()

        cmd = self.sys_argv[1]
        if not hasattr(self, cmd):
            print("invalid argument")
            self.help_msg()

    @staticmethod
    def help_msg():
        msg = """
        start           start FTP server
        stop            stop FTP server
        restart         restart FTP server
        creat user      creat a FTP user
        
        """
        exit(msg)

    def execute(self):
        """解析并执行指令"""
        print("--execute--")

        cmd = self.sys_argv[1]
        func = getattr(self, cmd)
        func()

    def start(self):
        """start ftp server"""
        server = main.FTPServer(self)
        server.run_forever()

    def stop(self):
        pass

    def restart(self):
        pass

    def creat_user(self):
        pass
