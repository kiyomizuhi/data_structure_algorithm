#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 17:36:33 2018

@author: hiroyukiinoue
"""

import random
import numpy as np

def quick_sort(A):
    return quick_sort_rec(A, 0, len(A) - 1)

def quick_sort_rec(A, l, r):
    if l < r:
        pivot, A = partition(A, l, r)
        A = quick_sort_rec(A, l, pivot - 1)
        A = quick_sort_rec(A, pivot + 1, r)
        return A
    else:
        return A

def swap(A, i, j):
    A[j], A[i] = A[i], A[j]
    return A

def partition(A, l, r):
    pivot = random.randrange(l, r + 1)
    A = swap(A, pivot, l)
    pivot = l
    i = l + 1
    j = i
    for curr in range(l + 1, r + 1):
        if A[curr] <= A[pivot]:
            A = swap(A, curr, i)
            i += 1
            j += 1
        else:
            j += 1
    A = swap(A, pivot, i - 1)
    pivot = i - 1
    return pivot, A


A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(quick_sort(A))

print(quick_sort(list(np.random.randint(500, size=16))))