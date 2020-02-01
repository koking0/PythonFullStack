#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/27 22:28
# @File     : ftp_server.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import sys

from core import management


def main():
    argv_parser = management.ManagementTool(sys.argv)
    argv_parser.execute()
