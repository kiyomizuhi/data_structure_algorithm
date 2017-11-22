#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 23:29:58 2017

@author: hiroyukiinoue
"""

'find subarrays with 0 sum'

import numpy as np

def find_zerosum_array(A):
    n = A.shape[0]
    S = np.zeros(n)
    idx = []
    for i in range(n):
        S[:i + 1] += A[i]
        zerosum = np.where(S[:i + 1] == 0)
        if zerosum[0].shape[0]:
            for j in zerosum[0]:
                idx.append([j, i])
    return idx

A = np.array([0, 1, 8, 9, -1, 1, -7, 1, 2, -10, 6, -7, 5, -10, -1, 3, 4, 2, 9, -4, -1])
idx = find_zerosum_array(A)
for i in idx:
    print(A[i[0]:i[1]+1])

        