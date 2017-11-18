#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 01:45:15 2017

@author: hiroyukiinoue
"""
import random

def quick_sort(A):
    quick_sort_rec(A, 0, len(A) - 1)
    return A
def quick_sort_rec(A, l, r):
    if l < r:
        pivot = partition(A, l, r)
        quick_sort_rec(A, l, pivot - 1)
        quick_sort_rec(A, pivot + 1, r)

def partition(A, l, r):
    pivot = random.randrange(l,r+1)
    swap(A, pivot, l)
    pivot = l
    l += 1
    for curr in range(l, r + 1):
        if A[curr] <= A[pivot]:
            swap(A, curr, l)
            l += 1
    swap(A, pivot, l-1)
    return l
    
def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp
    return A

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(quick_sort(A))