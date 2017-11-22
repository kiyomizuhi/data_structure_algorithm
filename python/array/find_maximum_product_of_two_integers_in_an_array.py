#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 18:52:12 2017

@author: hiroyukiinoue
"""

def function(A):
    if len(A) < 2:
        return None
    
    elif len(A) == 2:
        return A[0] * A[1]
    
    else:
        if A[0] >= A[1]:
            hmax1 = 0
            hmax2 = 1
            hmin1 = 1
            hmin2 = 0
        else:
            hmax1 = 1
            hmax2 = 0
            hmin1 = 0
            hmin2 = 1
        run = 2
        
        while run < len(A):
            if A[run] >= A[hmax1]:
                hmax2 = hmax1
                hmax1 = run
            elif A[run] > A[hmax2] and A[run] < A[hmax1]:
                hmax2 = run
            if A[run] <= A[hmin1]:
                hmin2 = hmin1
                hmin1 = run
            elif A[run] < A[hmin2] and A[run] > A[hmin1]:
                hmin2 = run
            run += 1
        
        p1 = A[hmax1] * A[hmax2]
        p2 = A[hmin1] * A[hmin2]
        if p1 >= p2:
            return p1, hmax1, hmax2
        else:
            return p2, hmin1, hmin2
        
A = [-10, 6, 9, -2, -5, 3, 2, 10, 4]
p, h1, h2 = function(A)
print('Prod : {}\nMax : {} at {}\nMin : {} at {}'.format(p, A[h1], h1, A[h2], h2))
print()