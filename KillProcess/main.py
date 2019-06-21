# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
    @name: main
    @author: Administrator
    @time: 2019/6/19 9:23
    @email: wolflikai@163.com
    @detail: ''
'''

"""
根据名字杀进程 可杀多进程应用
"""

import subprocess
import sys


def kill_all(app_name):
    if sys.platform == 'win32':
        cmd = 'taskkill /f /im {}.exe'.format(app_name)
    else:
        cmd = 'ps -e | grep "%s" | grep -v grep | awk \'{print $1}\'' % app_name
    ret = subprocess.check_output(cmd, shell=True)
    if ret:
        for line in ret.decode().split():
            ret = subprocess.run(f'kill -9 {line}', shell=True)
            if ret.returncode == 0:
                print(f'kill {line}')
    print('kill all finished')

if __name__ == '__main__':
    app_name = None
    if len(sys.argv) == 2:
        app_name = sys.argv[1]
    if app_name:
        kill_all(app_name)
    else:
        sys.exit()
