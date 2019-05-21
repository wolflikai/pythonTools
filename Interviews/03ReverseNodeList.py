#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019-05-21 23:23
@author : Kay Lee
@file   : 03ReverseNodeList.py 
@email  : wolflikai@163.com
@detail : None
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseList(head: ListNode) -> ListNode:
    """必须要一个临时变量接收 才会保留链表值"""
    p, cur = head, None
    while p:
        temp = p.next
        p.next = cur
        cur = p
        p = temp
    return cur