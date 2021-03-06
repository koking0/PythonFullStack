#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/30 下午7:51
# @Author   : alex
# @File     : encode.py
# @Project  : PythonFullStack
# @Software : PyCharm

string = "Alex  天津科技大学"

print(string.encode("utf-8"))
'''
b'Alex  \xe5\xa4\xa9\xe6\xb4\xa5\xe7\xa7\x91\xe6\x8a\x80\xe5\xa4\xa7\xe5\xad\xa6'

UTF-8编码 一个中文占三个字节
'''

print(string.encode("gbk"))
'''
b'Alex  \xcc\xec\xbd\xf2\xbf\xc6\xbc\xbc\xb4\xf3\xd1\xa7'

GBK编码 一个中文占两个字节
'''