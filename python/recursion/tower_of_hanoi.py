#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:12:59 2017

@author: hiroyukiinoue
"""

from stack import Stack

def tower_of_hanoi(tw, n, a, b, c):
    if n == 0:
        return
    tower_of_hanoi(tw, n - 1, a, c, b)
    tw[c].push(tw[a].pop().value)
    print_towers(tw)
    tower_of_hanoi(tw, n - 1, b, a, c)
    
def print_towers(tw):
    print(tw[0].stk.str_print_list())
    print(tw[1].stk.str_print_list())
    print(tw[2].stk.str_print_list())
    print('')
    
def prepare_stacks(n):
    tw = []
    tw.append(Stack())
    tw.append(Stack())
    tw.append(Stack())
    for i in range(n,0,-1):
        tw[0].push(i)
    return tw

if __name__ == '__main__':
    n = 3
    tw = prepare_stacks(n)
    print('')
    print_towers(tw)
    tower_of_hanoi(tw, n, 0, 1, 2)
else:
    print('tower_of_hanoi.py is imported')