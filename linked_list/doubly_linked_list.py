#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 18:29:04 2017

@author: hiroyukiinoue
"""

class Node():
    '''creat a node'''
    def __init__(self, value):
        self.value = value
        self.prevv = None
        self.nextt = None

    def set_value(self, value):
        '''set the value of the node'''
        self.value = value

    def get_value(self):
        '''get the value of the node'''
        return self.value

    def set_next(self, node):
        '''set the next node'''
        self.nextt = node

    def get_next(self):
        '''get the next node'''
        return self.nextt

    def set_prev(self, node):
        '''set the previous node'''
        self.prevv = node

    def get_prev(self):
        '''get the previous node'''
        return self.prevv


class DoubleLinkedList():
    '''creat a doubly linked list'''
    def __init__(self):
        self.head = None
        self.len = 0

    def show_the_list(self):
        '''print the content of the list'''
        if self.len == 0:
            print('This list is empty')
        elif self.len == 1:
            print('value = %d' % (self.head.value))
        else:
            temp = self.head
            while temp.get_next() != None:
                if temp == self.head:
                    print('          curr = %d, next = %d' \
                                          %(temp.value, temp.get_next().value))
                    temp = temp.get_next()
                else:
                    print('prev = %d, curr = %d, next = %d' \
                   %(temp.get_prev().value, temp.value, temp.get_next().value))
                    temp = temp.get_next()
            print('prev = %d, curr = %d' % (temp.get_prev().value, temp.value))

    def find_node(self, node):
        '''delete the head node of the list'''
        if self.len == 0:
            raise Exception('This list is empty')
        else:
            temp = self.head
            while temp.value != node.value:
                temp = temp.get_next()
                if temp is None:
                    return False
            return True

    def insert_at_head(self, node):
        '''insert a new node at the head of the list'''
        if self.len == 0:
            self.head = node
            self.len += 1
        else:
            temp = self.head
            temp.set_prev(node)
            node.set_next(temp)
            self.head = node
            self.len += 1

    def insert_at_tail(self, node):
        '''insert a new node at the head of the list'''
        if self.len == 0:
            self.head = node
            self.len += 1
        else:
            temp = self.head
            while temp.get_next() != None:
                temp = temp.get_next()
            temp.set_next(node)
            node.set_prev(temp)
            self.len += 1

    def insert_in_middle(self, middle, node):
        '''insert a new node right after "middle" node'''
        if self.len == 0:
            raise Exception('This list is empty and the specified node does not exist.')
        elif self.len == 1:
            if middle.value == self.head.value:
                middle.set_next(node)
                node.set_prev(middle)
                self.len += 1
            else:
                raise Exception('The specified node does not exist.')
        else:
            temp = self.head
            while temp.get_next().value != middle.value:
                temp = temp.get_next()
                if temp is None:
                    raise Exception('The specified node does not exist in this list.')
            temp = temp.get_next()
            if temp.get_next() is None:
                temp.set_next(node)
                node.set_prev(temp)
                self.len += 1
            else:
                nxt = temp.get_next()
                temp.set_next(node)
                node.set_prev(temp)
                nxt.set_prev(node)
                node.set_next(nxt)
                self.len += 1

    def delete_head_node(self):
        '''delete the head node of the list'''
        if self.len == 0:
            raise Exception('This list is empty')
        else:
            temp = self.head
            nxt = temp.get_next()
            self.head = nxt
            temp = None
            self.len -= 1

    def delete_tail_node(self):
        '''delete the tail node of the list'''
        if self.len == 0:
            raise Exception('This list is empty')
        elif self.len == 1:
            self.head = None
            self.len -= 1
        else:
            temp = self.head
            nxt = temp.get_next()
            while nxt.get_next() != None:
                temp = nxt
                nxt = nxt.get_next()
            temp.set_next(None)
            nxt = None
            self.len -= 1

    def delete_middle_node(self, middle):
        '''delete the specified node from the middle of the list'''
        if self.len == 0:
            raise Exception('This list is empty')
        elif self.len == 1:
            if middle.value == self.head.value:
                self.head = None
                self.len -= 1
            else:
                raise Exception('The specified node does not exist.')
        else:
            temp = self.head
            while temp.get_next().value != middle.value:
                temp = temp.get_next()
                if temp is None:
                    raise Exception('The specified node does not exist in this list.')
            mid = temp.get_next()
            nxt = mid.get_next()
            if nxt is None:
                temp.set_next(None)
                mid = None
                self.len -= 1
            else:
                temp.set_next(nxt)
                nxt.set_prev(temp)
                mid = None
                self.len -= 1

def __main():
    print('')
    kaka = DoubleLinkedList()
    for i in range(20):
        kaka.insert_at_tail(Node(i))
    kaka.show_the_list()
    print('')

if __name__ == "__main__":
    __main()
else:
    print('doubly_linked_list.py is imported')
