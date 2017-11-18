#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 23:41:10 2017

@author: hiroyukiinoue
"""

def insertion_sort1(A):
    for i in range(1, len(A), 1):
        temp = A[i]
        k = i
        while k > 0 and temp < A[k - 1]:
            A[k] = A[k - 1]
            k -= 1
        A[k] = temp
    return A

def insertion_sort2(A):
    for i in range(len(A) - 2, -1, -1):
        temp = A[i]
        k = i
        while k < len(A) - 1 and temp > A[k + 1]:
            A[k] = A[k + 1]
            k += 1
        A[k] = temp
    return A

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(insertion_sort1(A))
print('------------------------------------------')
A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(insertion_sort2(A))