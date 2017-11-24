#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 13:10:52 2017

@author: hiroyukiinoue
"""

class HashTable:
    def __init__(self, size):
        self.size = size
        self.slot = [None] * size
        self.data = [None] * size

    def hash_function(self, key):
        return key % self.size

    def rehash(self, oldhash, size):
        return (oldhash + 1) % size

    def put(self, key, data):
        hashvalue = self.hash_function(key)
        if self.slot[hashvalue] == None:
            self.slot[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slot[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nxt = self.rehash(hashvalue, self.size)
                while self.slot[nxt] != None and self.slot[nxt] != key:
                      nxt = self.rehash(nxt, self.size)
                if self.slot[nxt] == key:
                    self.data[nxt] = data
                else:
                    self.slot[nxt] = key
                    self.data[nxt] = data

    def get(self, key):
        hashvalue = self.hash_function(key)
        if self.slot[hashvalue] == None:
            return None
        elif self.slot[hashvalue] == key:
            return self.data[hashvalue]
        else:
            nxt = self.rehash(hashvalue, self.size)
            while self.slot[nxt] != key and nxt != hashvalue:
                nxt = self.rehash(nxt, self.size)
            if self.slot[nxt] == key:
                return self.data[nxt]
            elif nxt == hashvalue:
                print('Such key does not exist in this hashtable')
                return None


def __main():
    hs = HashTable(7)
    hs.put(54, 'kaka')
    hs.put(43, 'gugu')
    hs.put(23, 'pipi')
    hs.put(5, 'kggjg')
    print(hs.get(43))
    print(hs.slot)
    print(hs.data)

if __name__ == "__main__":
    __main()
else:
    print('hast_table.py is imported')
