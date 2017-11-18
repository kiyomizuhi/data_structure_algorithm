#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 05:38:13 2017

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


class SinglyLinkedList():
    """create a single linked list"""
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
            while current.get_next() != None:
                print('current = %d, next = %d' %\
                     (current.data, current.get_next().data))
                current = current.get_next()

    def get_node_by_data(self, data):
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

    def get_node_by_index(self, index):
        """fetch the node that you requested"""
        if self.head is None:
            print('The list is empty!')
        else:
            if index > self.count:
                raise ValueError('The list''s content is less than that!')
            current = self.head
            i = 0
            while i < index:
                current = current.get_next()
                i += 1
            return current.get_next()

    def insert_at_head(self, data):
        """insert a new node at the head"""
        if self.head is None:
            self.head = Node(data)
            self.count += 1
        else:
            temp = Node(data, self.head)
            self.head = temp
            self.count += 1

    def insert_at_tail(self, data):
        """insert a new node at the head"""
        if self.head is None:
            self.head = Node(data)
            self.count += 1
        else:
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(Node(data))
            self.count += 1

    def insert_in_middle_by_data(self, middle, data):
        """insert a new node in the middle right after node 'data'"""
        if self.head is None:
            self.head = Node(data)
            self.count += 1
        else:
            current = self.get_node_by_data(middle)
            temp = current.get_next()
            current.set_next(Node(data, temp))
            self.count += 1

    def insert_in_middle_by_index(self, index, data):
        """insert a new node in the middle right after node 'data'"""
        if self.head is None:
            self.head = Node(data)
            self.count += 1
        else:
            current = self.get_node_by_index(index)
            temp = current.get_next()
            current.set_next(Node(data, temp))
            self.count += 1

    def delete_head(self):
        """delete the head node"""
        if self.head is None:
            print('The list is empty!')
        else:
            temp = self.head
            self.head = temp.get_next()
            temp = None
            self.count -= 1

    def delete_tail(self):
        """delete the tail node"""
        if self.head is None:
            print('The list is empty!')
        else:
            prev = None
            current = self.head
            while current.get_next() != None:
                prev = current
                current = current.get_next()
            current = None
            prev.set_next(None)
            self.count -= 1

    def delete_tail_wo_prev(self):
        """delete the tail node"""
        if self.head is None:
            print('The list is empty!')
        elif self.count == 1:
            self.head = 0
        else:
            current = self.head
            while current.get_next().get_next() != None:
                current = current.get_next()
            current.set_next(None)
            self.count -= 1

    def delete_middle_by_data(self, middle):
        """delete a node (= data) from the middle"""
        if self.head is None:
            print('The list is empty!')
        elif self.count == 1:
            self.head = None
        else:
            prev = None
            current = self.head
            while current.get_next().data != middle:
                prev = current
                current = current.get_next()
                if current.get_next() is None and current.data != middle:
                    print('Such node does not exist in this list!')
                    return None
            prev = current
            current = current.get_next()
            prev.set_next(current.get_next())
            current = None
            self.count -= 1
            
    def delete_middle_by_index(self, index):
        """delete a node (= data) from the middle"""
        if self.head is None:
            print('The list is empty!')
        elif self.count == 1 and index == 0:
            self.head = None
        else:
            if index > self.count:
                raise ValueError('The list''s content is less than that!')
            prev = None
            current = self.head
            i = 0 
            while i < index:
                prev = current
                current = current.get_next()
                i += 1
            prev.set_next(current.get_next())
            current = None
            self.count -= 1
    
    def reverse_list(self):
        """Reverse the list"""
        prev = None
        current = self.head
        while current.get_next() != None:
            nnext = current.get_next()
            current.set_next(prev)
            prev = current
            current = nnext
        self.head = current
        current.set_next(prev)

    def reverse_list_recursive(self, node):
        """Reverse the list recursively"""
        if node.get_next() == None:
            self.head = node
            return node
        else:
            current =  self.reverse_list_recursive(node.get_next())
            current.set_next(node)
        

SLL = SinglyLinkedList()

SLL.insert_at_head(1)
SLL.insert_at_tail(2)
SLL.insert_at_tail(3)
SLL.insert_at_tail(4)
SLL.insert_at_tail(5)
SLL.insert_at_tail(6)
SLL.insert_at_tail(7)
SLL.insert_at_tail(8)
SLL.print_list()
print('')

SLL.reverse_list_recursive(SLL.head)
SLL.print_list()
print('')