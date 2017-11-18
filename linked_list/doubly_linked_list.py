#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 22:57:27 2017

@author: hiroyukiinoue
"""

class Node:
    """create a node"""
    def __init__(self, data, pprev=None, nnext=None):
        self.data = data
        self.prev = pprev
        self.next = nnext

    def get_data(self):
        """get the value of this node"""
        return self.data

    def set_data(self, data):
        """set the value of this node"""
        self.data = data

    def get_prev(self):
        """get the previous node"""
        return self.prev

    def set_prev(self, node):
        """set the previous node"""
        self.prev = node

    def get_next(self):
        """get the next node"""
        return self.next

    def set_next(self, node):
        """set the next node"""
        self.next = node


class DoublyLinkedList:
    """create a doubly linked list"""
    def __init__(self):
        self.head = None
        self.count = 0

    def print_list(self):
        """prints the content of this doubly linked list"""
        if self.head is None:
            print('It''s empty!')
        elif self.count == 1:
            print('prev =  , current = %d, next =  ' % (self.head.data))
        else:
            current = self.head
            while current.get_next() != None:
                if current.get_prev() != None:
                    print('prev = %d, current = %d, next = %d'\
        % (current.get_prev().data, current.data, current.get_next().data))
                else:
                    print('prev =  , current = %d, next = %d' \
        % (current.data, current.get_next().data))
                current = current.get_next()

    def insert_at_head(self, data):
        """inserts a new node with value data at the head of the list"""
        if self.head is None:
            self.head = Node(data)
            self.count += 1
        else:
            current = Node(data)
            current.set_next(self.head)
            self.head.set_next(current)
            self.head = current
            self.count += 1

    def insert_at_tail(self, data):
        """inserts a new node with value data at the end of the list"""
        if self.head is None:
            self.head = Node(data)
            self.count += 1
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(Node(data, current))
            self.count += 1

    def insert_in_middle(self, middle, data):
        """inserts a new node with value data in the middle of the list
        right after a node with value "middle"
        """
        if self.head is None and middle != 0:
            print('The list is empty!')
            return None
        elif self.head is None and middle == 0:
            self.head = Node(data)
            self.count += 1
        else:
            middle = self.get_node(middle)
            middle_next = middle.get_next()
            temp = Node(data, middle, middle_next)
            middle.set_next(temp)
            middle_next.set_prev(temp)

    def get_node(self, node):
        """return a node with value "node" """
        if self.head is None:
            print('The list is empty!')
            return None

        current = self.head
        while current.get_next().data != node:
            current = current.get_next()
        
        if current == None:
            raise Exception('Such node does not exist in this list!')
        else:
            return current.get_next()

    def delete_head(self):
        """delete the node at the head"""
        if self.head is None:
            raise Exception('The list is empty!')
        elif self.count == 1:
            self.head = None
            self.count -= 1
        else:
            temp = self.head
            self.head = temp.get_next()
            temp.get_next().set_prev(None)
            temp = None
            self.count -= 1

    def delete_tail(self):
        """delete the node at the tail"""
        if self.head is None:
            raise Exception('The list is empty!')
        elif self.count == 1:
            self.head = None
            self.count -= 1
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.get_prev().set_next(None)
            current = None
            self.count -= 1

    def delete_middle(self, middle):
        """delete the node with data "middle" in the middle of the list"""
        if self.head is None:
            raise Exception('The list is empty!')
        elif self.count == 1:
            self.head = None
            self.count -= 1
        else:
            current = self.head
            while current.get_next().data != middle:
                current = current.get_next()
            current = current.get_next()
            current_prev = current.get_prev()
            current_next = current.get_next()
            current_prev.set_next(current_next)
            current_next.set_prev(current_prev)
            current = None
            self.count -= 1


DLL = DoublyLinkedList()
DLL.insert_at_head(1)
DLL.insert_at_tail(2)
DLL.insert_at_tail(3)
DLL.insert_at_tail(4)
DLL.insert_at_tail(5)
DLL.insert_at_tail(6)
DLL.insert_at_tail(7)
DLL.insert_at_tail(8)
DLL.insert_in_middle(5, 15)
DLL.print_list()
print('')
DLL.delete_head()
DLL.print_list()
print('')
DLL.delete_tail()
DLL.print_list()
print('')
DLL.delete_middle(15)
DLL.print_list()
