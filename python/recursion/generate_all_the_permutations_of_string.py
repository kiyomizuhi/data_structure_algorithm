#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 15:00:42 2017

@author: hiroyukiinoue
"""

def function(s):
    if len(s) == 1:
        return [s]
    else:
        p, r = s[0], s[1:]
        rr = function(r)
        st = [x[:j] + p + x[j:] for x in rr for j in range(len(x)+1)]
        return st

print(function('abc'))