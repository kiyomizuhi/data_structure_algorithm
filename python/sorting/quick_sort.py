#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 02:36:57 2017

@author: hiroyukiinoue
"""

import random

def quick_sort(A):
    return quick_sort_real(A, 0, len(A) - 1)

def quick_sort_real(A, low, high):
    if low < high:
        pivot = partition(A, low, high)
        quick_sort_real(A, low, pivot - 1)
        quick_sort_real(A, pivot + 1, high)
        return A
    else:
        return A

def partition(A, low, high):
    swap(A, low, high)
    for i in range(low, high):
        if A[i] <= A[high]:
            swap(A, i, low)
            low += 1
    swap(A, low, high)
    return low

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(quick_sort(A))

b = list(range(1000))
random.shuffle(b)
print(quick_sort(b))