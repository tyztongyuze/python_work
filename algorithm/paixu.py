# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : paixu.py
@ Date & Time   : 2020/7/26 21:33
@ Description   : None
"""

n, x, flag = int(input()), [int(v) for v in input().split()], int(input())

y = [str(v) for v in sorted(x, reverse=flag)]
print(' '.join(y))
