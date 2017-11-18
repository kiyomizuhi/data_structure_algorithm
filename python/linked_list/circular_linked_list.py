#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 01:50:13 2017

@author: hiroyukiinoue
"""

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


class CircularLinkedList():
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

    def loop_to_nth_last_node(self, n):
        if n > self.len:
            raise Exception('The length of this list is less than the specified number')
        elif n <= 1:
            raise Exception('You have to pass an integer bigger than 1.')
        else:
            temp = self.head
            nxt = temp
            for _ in range(1,n):
                nxt = nxt.get_next()
            while nxt.get_next() != None:
                temp = temp.get_next()
                nxt = nxt.get_next()
            nxt.set_next(temp)
    
    def find_loop_head(self):
        '''delete the specified node from the middle of the list'''
        if self.len == 0:
            raise Exception('This list is empty.')
        elif self.len == 1:
            raise Exception('Only one element in this list.')
        run1 = self.head.get_next()
        run2 = self.head.get_next().get_next()
        while run1.value != run2.value:
            run1 = run1.get_next()
            run2 = run2.get_next().get_next()
            if run2 is None:
                print('No loop in this list.')
                break
        if run2 != None:
            run1 = self.head
            while run1.value != run2.value:
                run1 = run1.get_next()
                run2 = run2.get_next()
                return run1


def __main():
    print('')
    kaka = CircularLinkedList()
    for i in range(50):
        kaka.insert_at_tail(Node(i))
    kaka.show_the_list()
    print('')
    
    kaka.loop_to_nth_last_node(11)
    lph = kaka.find_loop_head()
    print(lph.value)

if __name__ == "__main__":
    __main()
else:
    print('circular_linked_list.py is imported')
            