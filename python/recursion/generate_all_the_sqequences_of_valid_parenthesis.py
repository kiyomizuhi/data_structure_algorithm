#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 21:39:52 2017

@author: hiroyukiinoue
"""

def function(L, R):
    if L == 0 and R == 0:
        return ['']
    elif L > R:
        return ['']
    elif L == 0 and R != 0:
        return [')' * R]
    elif L != 0 and L < R:
        l = ['(' + x for x in pare(L - 1, R)]
        r = [')' + x for x in pare(L, R - 1)]
        return l + r
    elif L == R and L != 0:
        return ['(' + x for x in pare(L - 1, R)]

def main():
    n = 3
    print(function(n, n))

if __name__ == '__main__':
    main()
