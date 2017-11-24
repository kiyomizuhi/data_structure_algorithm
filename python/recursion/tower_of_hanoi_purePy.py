#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 13:06:19 2017

@author: hiroyukiinoue
"""

global count

def tower_of_hanoi(tw, n, a, b, c):
    if n == 0:
        return
    tower_of_hanoi(tw, n - 1, a, c, b)
    tw[c].append(tw[a].pop())
    print_towers(tw)
    tower_of_hanoi(tw, n - 1, b, a, c)
    
def print_towers(tw):
    global count
    print(tw[0])
    print(tw[1])
    print(tw[2])
    print('')
    count += 1
    
def initialize(n):
    tw = list(range(n, 0, -1))
    return [tw, [], []]

if __name__ == '__main__':
    n = 4
    tw = initialize(n)
    print('')
    print_towers(tw)
    count = 0
    tower_of_hanoi(tw, n, 0, 1, 2)
    print('# of operations = %d' % (count))
else:
    print('tower_of_hanoi.py is imported')