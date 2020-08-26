# !/usr/bin/python3
# -*- coding: utf-8 -*-

"""
@ Author        : tongyuze
@ Project       : algorithm
@ FileName      : search_2.py
@ Date & Time   : 2020/8/25 17:02
@ Description   : 二分查找
"""


def search2(n, v, a):

    if n == 0:
        return -1

    midp = n // 2
    if a[midp] == v:
        while a[midp - 1] == v:
            midp -= 1
        return midp
    elif a[midp] > v:
        return search2(midp, v, a[:midp])
    else:
        return search2(n-midp-1, v, a[midp+1:])


def search_22(n, v, a):
    if v > a[n-1]:
        return n+1
    l, r = 0, n
    while l < r:
        mid = (l + r) // 2
        if v > a[mid]:
            l = mid + 1
        elif v <= a[mid]:
            r = mid
    return r+1


x = search2(6, 4, [1, 2, 2, 3, 5, 6])
print(x)
