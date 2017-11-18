#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:41:58 2017

@author: hiroyukiinoue
"""


def selection_sort1(A):
    for i in range(len(A)-1):
        minn = i
        for j in range(i, len(A), 1):
            if A[minn] >= A[j]:
                minn = j
        swap(A, i, minn)
    return A

def selection_sort2(A):
    for i in range(len(A)-1, 0, -1):
        maxx = i
        for j in range(i, -1, -1):
            if A[maxx] <= A[j]:
                maxx = j
        swap(A, i, maxx)
    return A

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A
    
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(selection_sort1(A))
print('------------------------------------------')
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(selection_sort2(A))