#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 02:02:40 2017

@author: hiroyukiinoue
"""

class Node():
    """create a node"""
    def __init__(self, data, nnext=None):
        self.data = data
        self.next = nnext

    def get_data(self):
        """get the value of this node"""
        return self.data

    def set_data(self, data):
        """set the value of this node"""
        self.data = data

    def get_next(self):
        """get the next node"""
        return self.next

    def set_next(self, node):
        """set the next node"""
        self.next = node


class CircularlyLinkedList():
    """creat a circularly linked list"""
    def __init__(self):
        self.head = None
        self.count = 0
    
    def print_list(self):
        """print out the content of the list"""
        if self.head is None:
            print('The list is empty!')
        elif self.count == 1:
            print('current = %d, next =  ' % (self.head.data))
        else:
            current = self.head
            while current.get_next() != self.head:
                print('current = %d, next = %d' %\
                     (current.data, current.get_next().data))
                current = current.get_next()

    def get_node(self, data):
        """fetch the node that you requested"""
        if self.head is None:
            print('The list is empty!')
        else:
            current = self.head
            while current.get_next().data != data:
                current = current.get_next()
                if current.get_next() is None and current.data != data:
                    print('Such node does not exist in this list!')
                    return None
            return current.get_next()
        
    
