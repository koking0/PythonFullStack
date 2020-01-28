#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/27 22:28
# @File     : settings.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import os

MAX_SOCKET_LISTEN = 5
HOST = "0.0.0.0"
PORT = 9999

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ACCOUNT_FILE = "%s/conf/accounts.ini" % BASE_DIR
USER_HOME_DIR = os.path.join(BASE_DIR, "home")
