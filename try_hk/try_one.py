#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18-9-25 下午1:19
# @Author  : ShaoXin
# @Summary :
# @Software: PyCharm
from time import sleep

from pykeyboard import PyKeyboard

k = PyKeyboard()


def double(key):
    k.tap_key(key, n=2, interval=1)


def union(a, b, interval=0.5):

    k.tap_key(a)
    sleep(interval)
    k.tap_key(b)


if __name__ == '__main__':
    while 1:
        a = input()
        double(a)
    # union('c', 'a')
