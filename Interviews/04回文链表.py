# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
    @name: 04回文链表
    @author: Administrator
    @time: 2019/5/22 10:39
    @email: wolflikai@163.com
    @detail: ''
'''

"""
请判断一个链表是否为回文链表。
1->2->2->1 true
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def isPalindrome(head: ListNode) -> bool:
    res = []
    if not head:
        return True
    node = head
    while node:
        res.append(node.val)
        node = node.next
    return res == res[::-1] # 只要比较结点值即可