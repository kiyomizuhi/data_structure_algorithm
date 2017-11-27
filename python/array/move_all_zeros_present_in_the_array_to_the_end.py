#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def function(A):
    hd1 = 0
    hd2 = A.shape[0] - 1
    while hd1 < hd2:
        if A[hd1] == 0:
            # A[hd1], A[hd2] = A[hd2], A[hd1] 
            temp  = A[hd2]
            A[hd2] = A[hd1]
            A[hd1] = temp
            hd2 -= 1
        else:
            hd1 += 1
    return A
            
def main():
    A = np.random.randint(5, size=20)
    print(function(A))

if __name__ == '__main__':
    main()
     
    