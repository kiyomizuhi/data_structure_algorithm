#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:04:30 2017

@author: hiroyukiinoue
"""


def subs(s):
    if s == []:
        return [[]]
    else:
        h, r = s[0], s[1:]
        sr = subs(r)
        sh = [[h] + ss for ss in sr]
        return sh + sr 

print(subs([1, 2, 3, 4, 5]))