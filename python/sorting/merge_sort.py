#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 01:29:19 2017

@author: hiroyukiinoue
"""
import random

def merge_sort(A):
    """assuming len(A) >= 2"""
    if len(A) <= 1:
        return A
    else:
        mid = len(A)//2
        left = A[:mid]
        right = A[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1
        return A

A = [534, 246, 933, 127, 277, 321, 454, 565, 220]
print(merge_sort(A))
b = list(range(1000))
random.shuffle(b)
print(merge_sort(b))
        
            
    
    