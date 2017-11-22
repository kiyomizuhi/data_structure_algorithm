#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 01:09:32 2017

@author: hiroyukiinoue
"""

#sort binaryarray in linear time

import numpy as np

def function(A):
    hd1 = 0
    hd2 = len(A) - 1
    while hd1 != hd2:
        if A[hd1] == 0:
            hd1 += 1
        else:
            temp = A[hd2]
            A[hd2] = A[hd1]
            A[hd1] = temp
            hd2 -= 1
    return A

A = np.random.randint(2, size=50)
print('input = ', A)
print()
A = function(A)
print('output = ',A)

            