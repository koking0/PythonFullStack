#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2019/12/21 下午2:42
# @Author   : alex
# @File     : 三级菜单.py
# @Project  : PythonFullStack
# @Software : PyCharm

menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}

CurrentMenu = menu
ParentList = []
while True:
    for i in CurrentMenu:
        print(i)
    select = input("——> ").strip()
    if select in CurrentMenu:
        ParentList.append(CurrentMenu)
        CurrentMenu = CurrentMenu[select]
    elif select.lower()[0] == 'q':
        break
    elif select.lower()[0] == 'b' and ParentList:
        CurrentMenu = ParentList.pop()
    else:
        print("No such menu!\n")