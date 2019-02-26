#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 19/2/26 20:38
@author : Kay Lee
@file   : main.py 
@email  : wolflikai@163.com
@detail : None
'''


import fileinput
import sys

def change_string(filepath, old, new, backup_suffix):
    '''
    :param filepath: file_path str
    :param old: str
    :param new: str
    :param backup_suffix: backup_suffix='.bak' ==>> example.txt -> example.txt.bak
    '''
    for line in fileinput.input(filepath, inplace=True, backup=backup_suffix):
        line = line.replace(old, new)
        sys.stdout.write(line)

if __name__ == '__main__':
    change_string('example.txt', '#', '//', '.bak')
