#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 00:47:50 2017

@author: hiroyukiinoue
"""

import numpy as np

def function(A, sm):
    idx = 0
    lng = 0
    sms = np.zeros(A.shape[0])
    for i in range(A.shape[0]):
        sms[:i + 1] += A[i]
        for j in range(i):
            if (sms[j] == sm) and i - j + 1 > lng:
                idx = [j, i]
                lng = i - j + 1
    if lng == 0:
        return None
    return idx

def main(A, sm):
    print('\nfind the longest subarray that sums to " %d "' % (sm))
    print(A)
    idx = function(A, sm)
    if idx is None:
        print('there is no subarray with the given sum.')
        return None
    print('\nfound           : ', A[idx[0]:idx[1] + 1])
    print('that sums to    : ', A[idx[0]:idx[1] + 1].sum())
    print('with the length : ', idx[1]- idx[0] + 1)

if __name__ == '__main__':
    A = np.random.randint(10, size=20) - 5
    sm = np.random.randint(10, size=1) - 5
    main(A, sm)