#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 16:43:32 2017

@author: hiroyukiinoue
"""

import sys

def function_traverse_from_right(A):
    diff = -sys.maxsize-1
    hd = len(A) - 1
    run = len(A) - 1
    
    while run >= 0:
        if A[run] >= A[hd]:
            hd = run
        elif diff < max(diff, A[hd] - A[run]):
            diff = A[hd] - A[run]
            hdmax = hd
            hdmin = run
        run -= 1
    
    return diff, hdmax, hdmin

def function_traverse_from_left(A):
    diff = -sys.maxsize-1
    hd = 0
    run = 0
    
    while run < len(A):
        if A[run] <= A[hd]:
            hd = run
        elif diff < max(diff, A[run] - A[hd]):
            diff = A[run] - A[hd]
            hdmax = run
            hdmin = hd
        run += 1
    
    return diff, hdmax, hdmin

A = [2, 7, 9, 5, 1, 3, 5]
diff, hdmax, hdmin = function_traverse_from_right(A)
print('Dif : {}\nMax : {} at {}\nMin : {} at {}'.format(diff, A[hdmax], hdmax, A[hdmin], hdmin))
print()
diff, hdmax, hdmin = function_traverse_from_left(A)
print('Dif : {}\nMax : {} at {}\nMin : {} at {}'.format(diff, A[hdmax], hdmax, A[hdmin], hdmin))