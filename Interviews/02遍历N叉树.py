#!/usr/bin/python3
# -*- coding:utf-8 -*-
'''
@time   : 2019-05-21 23:00
@author : Kay Lee
@file   : 02遍历N叉树.py 
@email  : wolflikai@163.com
@detail : None
'''

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

"""
给定一个 N 叉树，返回其节点值的后序遍历。

解题思路:
使用两个列表
"""

class Solution:
    def post_order(self, root:Node) -> list[int]:
        lists = []
        stack = []
        if root is None:
            return []
        lists = [root]
        while lists:
            cur = lists.pop()
            stack.append(cur)
            if cur.children:
                lists.append(cur.children)
        """这时lists为空 可以用来存结果 stack为排好序的节点列表"""
        while stack:
            cur = stack.pop()
            lists.append(cur.val)
        return lists
