#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np

def function(A):
    N = A.shape[0]
    poles = []
    hd1 = 0
    hdmax = 0
    while hd1 < N:
        hd2 = hd1 + 1
        if hd2 == N:
            if hd1 == hdmax:
                poles.append(hd1)
            break
        hdmax = hd1
        while hd2 < N:
            if A[hd2] >= A[hdmax]:
                hdmax = hd2
            if A[hd2] < A[hd1]:
                break
            hd2 += 1
        if hd2 == N:
            poles.append(hd1)
            hd1 += 1
        else:
            while hd2 < N:
                if A[hd2] >= A[hdmax]:
                    hdmax = hd2
                    break
                hd2 += 1
            if hd2 == N:
                break
            else:
                hd1 = hdmax
    return poles
            
def main_sub(n):
    A = np.random.randint(n, size=n)
    #A = np.array([3, 2, 4, 6, 5, 7, 8, 7])
    assert(A.shape[0] >= 2)
    poles = function(A)
    return poles, A

def main():
    arrs = []
    n = 15
    nran = set(range(n//3, 2*n//3))
    for _ in range(100000):
        poles, A = main_sub(n)
        if len(poles) > 0 and set(poles) < nran:
            arrs.append([A, poles])

    for arr in arrs:
        A, poles = arr[0], arr[1]
        print('\nA =', A)
        for i in poles:
            print('pole : A[{}] = {}'.format(i, A[i]))

if __name__ == '__main__':
    main()
     
    