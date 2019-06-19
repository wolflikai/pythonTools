#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019-06-19 21:15
@author : Kay Lee
@file   : main.py 
@email  : wolflikai@163.com
@detail : None
'''
import datetime

"""
现在最近的30分或整点--电商中常用
"""
import datetime
def get_next_valid_datetime(time):
    timestamp = (time.timestamp()+1799) // 1800 * 1800
    return datetime.datetime.fromtimestamp(timestamp)

print(get_next_valid_datetime(datetime.datetime.now()))




