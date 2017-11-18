#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 22:42:08 2017

@author: hiroyukiinoue
"""

class Node():
    '''creat a node'''
    def __init__(self, value):
        self.value = value
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


class SingleLinkedList():
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
                print('curr = %d, next = %d' % (temp.value, temp.get_next().value))
                temp = temp.get_next()
            print('curr = %d' % (temp.value))

    def str_print_list(self):
        '''print the content of the list'''
        if self.len == 0:
            return '|'
        else:
            temp = self.head
            strr = ''
            while temp.get_next() != None:
                strr += str(temp.value) + ' ,'
                temp = temp.get_next()
            strr += str(temp.value) + '|'
            return strr[::-1]

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
            self.len += 1

    def insert_in_middle(self, middle, node):
        '''insert a new node right after "middle" node'''
        if self.len == 0:
            raise Exception('This list is empty and the specified node does not exist.')
        elif self.len == 1:
            if middle.value == self.head.value:
                middle.set_next(node)
                self.len += 1
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
                mid.set_next(node)
                self.len += 1
            else:
                mid.set_next(node)
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
            prev = temp
            mid = temp.get_next()
            nxt = mid.get_next()
            if nxt is None:
                prev.set_next(None)
                mid = None
                self.len -= 1
            else:
                prev.set_next(nxt)
                mid = None
                self.len -= 1

    def delete_middle_node_without_prev(self, middle):
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
            while temp.value != middle.value:
                temp = temp.get_next()
                if temp is None:
                    raise Exception('The specified node does not exist in this list.')
            mid = temp
            nxt = temp.get_next()
            if nxt is None:
                mid = None
                self.len -= 1
            else:
                mid.value = nxt.value
                mid.set_next(nxt.get_next())
                nxt = None
                self.len -= 1

    def delete_nth_last_node(self, n):
        if n > self.len:
            raise Exception('The length of this list is less than the specified number')
        elif n <= 0:
            raise Exception('You have to pass an positive integer.')
        elif n == 1:
            self.delete_tail_node()
        else:
            temp = self.head
            nxt = temp
            for i in range(1,n):
                nxt = nxt.get_next()
            while nxt.get_next() != None:
                temp = temp.get_next()
                nxt = nxt.get_next()
            mid = temp
            nxt = temp.get_next()
            if nxt is None:
                mid = None
                self.len -= 1
            else:
                mid.value = nxt.value
                mid.set_next(nxt.get_next())
                nxt = None
                self.len -= 1

    def pop_head_node(self):
        '''delete the head node of the list'''
        if self.len == 0:
            return None
        else:
            temp = self.head
            self.head = temp.get_next()
            self.len -= 1
            return temp

    def erase_dups(self):
        '''delete the head node of the list'''
        temp = self.head
        run = self.head
        while temp.get_next() != None:
            while run.get_next() != None:
                temp = temp.get_next()

    def erase_dups_hash(self):
        if self.len == 0:
            return True
        if self.len == 1:
            return True
        from hash_table import HashTable
        hsh = HashTable(23)
        temp = self.head
        hsh.put(temp.value, 1)
        nxt = temp.get_next()
        while nxt.get_next() != None:
            cnt = hsh.get(nxt.value)
            if cnt is None:
                hsh.put(nxt.value, 1)
            else:
                cnt += 1
                hsh.put(temp.value, cnt)
                temp.value = temp.get_next().value
                temp.set_next(nxt.get_next())
            temp = nxt
            nxt = nxt.get_next()

def convert_to_list(n):
    if type(n) != int:
        raise Exception('You must pass an integer')
    else:
        ill = SingleLinkedList()
        while n//10 != 0:
            r = n % 10
            n = n // 10
            ill.insert_at_tail(Node(r))
        ill.insert_at_tail(Node(n))
        return ill

def add_two_lists(ls1, ls2):
    ls = SingleLinkedList()
    carry = 0
    while not(ls1.len == 0 and ls2.len == 0):
        if ls1.len == 0:
            d1 = 0
        else:
            d1 = ls1.pop_head_node().value
        if ls2.len == 0:
            d2 = 0
        else:
            d2 = ls2.pop_head_node().value
        ad = d1 + d2
        r = ad % 10
        ls.insert_at_tail(Node(r+carry))
        carry = ad // 10
    if carry == 1:
        ls.insert_at_tail(Node(carry))
    return ls
            
def __main():
    print('')
    kaka = SingleLinkedList()
    for i in range(10):
        kaka.insert_at_tail(Node(i))
    kaka.show_the_list()
    print('')
    strr = kaka.str_print_list()
    print(strr)
    
    #ls = add_two_lists(convert_to_list(1234), convert_to_list(456))
    #ls.show_the_list()
    #print('')
    
    kaka.insert_in_middle(Node(5), Node(5))
    kaka.show_the_list()
    print('')
    kaka.erase_dups_hash()
    kaka.show_the_list()
    print('')

if __name__ == "__main__":
    __main()
else:
    print('singly_linked_list.py is imported')
