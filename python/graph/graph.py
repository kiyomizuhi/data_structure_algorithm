#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict

class Vertex:
    def __init__(self, node=0):
        self.id  = node
        self.adj = {}
        self.dst = sys.maxsize
        self.vst = 0
        self.prv = None
    
    def set_visit(self, visit):
        self.vst = visit
        
    def get_visit(self):
        return self.vst
    
    def set_distance(self, dist):
        self.dst = dist
        
    def get_distance(self):
        return self.dst
    
    def set_prev(self, prev):
        self.prv = prev
        
    def get_prev(self):
        return self.prv

class Graph:
    def __init__(self, edges):
        self.nds = defaultdict(lambda: Vertex())
        self.num_nds = 0
        
        for edge in edges:
            if len(edge) == 2:
                self.add_edge(edge[0], edge[1])
            elif len(edge) == 3:
                self.add_edge(edge[0], edge[1], edge[2])
    
    def add_edge(self, frm, to, wght=1):
        self.nds[frm].adj[to] = wght

if __name__== '__main__':
    print('main')
else:
    print('"loaded graph and vertex classes"')
    
        