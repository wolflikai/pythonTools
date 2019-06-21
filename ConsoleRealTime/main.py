# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
    @name: main
    @author: Administrator
    @time: 2019/6/21 14:15
    @email: wolflikai@163.com
    @detail: ''
'''

"""
命令行实时输出
"""

import subprocess
import sys


def get_realtime_output(cmd):
    p = subprocess.Popen(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    if sys.platform == 'win32':
        encode_style = 'gbk'
    else:
        encode_style = 'utf-8'
    while True:
        output = p.stdout.readline()
        if output == b'' and p.poll() is not None:
            break
        if output:
            print(output.decode(encode_style).strip())


if __name__ == '__main__':
    test = 'ping www.baidu.com -t'
    get_realtime_output(test)
