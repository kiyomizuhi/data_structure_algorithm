#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 00:19:07 2017

@author: hiroyukiinoue
"""

def shell_sort1(A):
    incr = len(A)//2
    while incr > 0:
        for start in range(incr):
            gap_insertion_sort1(A, start, incr)
        incr = incr // 2
    return A

def gap_insertion_sort1(A, start, gap):
    for i in range(start + gap, len(A), gap):
        temp = A[i]
        k = i
        while k >= gap and temp <= A[k - gap]:
            A[k] = A[k - gap]
            k -= gap
        A[k] = temp
    return A

def shell_sort2(A):
    incr = len(A)//2
    while incr > 0:
        for start in range(len(A)-1, len(A) - 1 - incr, -1):
            gap_insertion_sort2(A, start, incr)
        incr = incr // 2
    return A

def gap_insertion_sort2(A, start, gap):
    for i in range(start - gap, -1, -gap):
        temp = A[i]
        k = i
        while k <= len(A) -1 - gap and temp >= A[k + gap]:
            A[k] = A[k + gap]
            k += gap
        A[k] = temp
    return A

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(shell_sort1(A))
print('------------------------------------------')
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(shell_sort2(A))