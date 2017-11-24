#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:45:48 2017

@author: hiroyukiinoue
"""

from hash_table import HashTable

def anagram(st1, st2):
    if len(st1) != len(st2):
        return False
    else:
        hs = HashTable(255)
        for i, j in zip(st1, st2):
            hs[ord(i)] = 1
            hs[ord(j)] = -1  