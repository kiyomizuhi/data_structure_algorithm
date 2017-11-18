#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 00:14:36 2017

@author: hiroyukiinoue
"""

def bubble_sort1(A):
    for i in range(len(A)-1, 1, -1):
        for j in range(i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)
    return A

def bubble_sort2(A):
    for i in range(len(A)):
        for j in range(len(A) - 1, i, -1):
            if A[j] < A[j - 1]:
                swap(A, j, j - 1)
    return A

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A
    
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(bubble_sort1(A))
print('------------------------------------------')
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(bubble_sort2(A))