# !/usr/bin/python3
# -*- coding:utf-8 -*-
'''
    @name: 05字符串相加
    @author: Administrator
    @time: 2019/5/22 10:46
    @email: wolflikai@163.com
    @detail: ''
'''


"""
两个字符串数字 实现相加
"""

def stringAdd(num1:str, num2:str) -> str:
    num1, num2 = num1[::-1], num2[::-1]
    m, n = len(num1), len(num2)
    res = ''
    carry = 0
    for i in range(max(m, n)):
        n1 = ord(num1[i]) - ord('0') if i < m else 0
        n2 = ord(num2[i]) - ord('0') if i < n else 0
        s = n1 + n2 + carry
        carry, r = s // 10, s % 10
        res = str(r) + res


    if carry:
        res = str(carry) + res
    return res

if __name__ == '__main__':
    ret = stringAdd('898', '323')
    assert ret == '1221'

