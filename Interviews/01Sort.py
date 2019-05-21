#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019-05-21 21:27
@author : Kay Lee
@file   : 01.py 
@email  : wolflikai@163.com
@detail : None
'''

def buddleSort(ls:list):
    for i in range(len(ls)):
        for j in range(len(ls)-1):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]


def buddleSort2(ls:list):
    """
    优化
    :param ls:
    :return:
    """
    for i in range(len(ls)-1):
        flag = True
        for j in range(len(ls)-1-i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
                flag = False
        if flag == True:
            break

def sel_sort(ls):
    for i in range(len(ls)):
        max_index = i
        max_val = ls[max_index]
        for j in range(i+1, len(ls)):
            if ls[j] > max_val:
                max_index = j
                max_val = ls[j]
        if max_index != i:
            ls[i], ls[max_index] = ls[max_index], ls[i]

def insert_sort(ls:list):
    for i in range(1, len(ls)):
        temp = ls[i]
        while i > 0 and ls[i-1] > temp:
            ls[i] = ls[i-1]
            i -= 1
        ls[i] = temp


if __name__ == '__main__':
    ls = [9,8,7,6,3,5]
    insert_sort(ls)
    print(ls)
