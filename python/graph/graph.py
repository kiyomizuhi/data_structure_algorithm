#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

class Node:
    """class of node.
       for unweighted graphs: weight = 1
       for weighted graphs: weight should be given from data.
    """

    def __init__(self, idx = 0):
        self.id = idx
        self.neighbors = {}
        self.distance = sys.maxsize
        self.visit = 0
        self.prev = None
        
    
    def set_visit(self, vst):
        ''' this method sets the visited status of the node'''
        self.visit = vst


    def get_visit(self):
        ''' this method returns the visited status of the node'''
        return self.visit


    def set_distance(self, dist):
        ''' this method sets the distance from the previous node'''
        self.distance = dist


    def get_distance(self):
        ''' this method returns the distance from the previous node'''
        return self.distance


    def set_prev(self, prev):
        ''' this method sets the previous node'''
        self.prev = prev


    def get_prev(self):
        ''' this method returns the previous node'''
        return self.prev


    def get_neighbors(self):
        ''' this method returns the adjacent nodes'''
        return self.neighbors

 
    def add_neighbor(self, nbr, wght=1):
        ''' this method adds a node to adjacent nodes'''
        self.neighbors[nbr] = wght


    def __str__(self):
        ''' this method returns a string of neighboring nodes'''
        return str(self.id) + ' connectedTo: ' \
                            + str([x for x in self.neighbors])


class UndirectedGraph:
    """class of undirected graph.
       for unweighted graphs: weight = 1
       for weighted graphs: weight should be given from data.
    """
    
    def __init__(self, edges):
        self.nds = defaultdict(lambda: Node())
        self.num_nds = len(self.nds)
        
        for edge in edges:
            if len(edge) == 2:
                self.add_edge(edge[0], edge[1])
            elif len(edge) == 3:
                self.add_edge(edge[0], edge[1], edge[2])


    def add_edge(self, frm, to, wght=1):
        """add an edge
        
        # Arguements
            frm: node that the edge comes from.
            to: node that the edge goes to.
            wght: 1 unless specified
        # Returns
            None.
        """
        self.nds[frm].add_neighbor(to, wght)
        self.nds[to].add_neighbor(frm, wght)


    def get_node(self, nd):
        """return the pointer or node itself.
        
        # Arguements
            nd: The id of the node.
                
        # Returns
            node itself if in or None if not in
        """
        if nd in self.nds:
            return self.nds[nd]
        else:
            return None


    def retrieve_path(self, nd):
        """place nodes on a circumference
        
        # Arguements
            num_nodes: number of nodes.
            
        # Returns
            2D coordinates of the nodes.
        """
        if self.nds[nd].prev is None:
            return [nd]
        else:
            prev = self.nds[nd].get_prev()
            path = self.retrieve_path(prev)
            path.append(nd)
            return path


class Stack:
    """class of queue.
       For example, dfs uses this.
       items keeps the stack data
    """
    
    def __init__(self):
        self.items = []


    def isEmpty(self):
        ''' this method checks if the item is empty'''
        return self.items == []


    def push(self, item):
        ''' push a new item on the top of stack'''
        self.items.append(item)


    def pop(self):
        ''' pop the top item from the stack'''
        return self.items.pop()


    def peek(self):
        ''' look at the top of the stack without popping'''
        return self.items[len(self.items)-1]


    def size(self):
        ''' returns the size of the stack '''
        return len(self.items)
     

class Queue:
    """class of queue.
       For example, bfs uses this.
       items keeps the queue data
    """
    
    def __init__(self):
        self.items = []


    def isEmpty(self):
        ''' this method checks if the item is empty'''
        return self.items == []


    def enqueue(self, item):
        ''' enqueue a new node at the end (placed at the head)'''
        self.items.insert(0, item)


    def dequeue(self):
        ''' dequeue the first node (placed at the tail)'''
        return self.items.pop()


    def size(self):
        ''' returns the size of the queue '''
        return len(self.items)


class GraphData:
    """class to load the graph data
       The data was obtained from Sedgewick's website
       https://algs4.cs.princeton.edu/
       largeG:  1000000 nodes  7586063 edges
       mediumG:     250 nodes     1273 edges
       tinyG:        13 nodes       13 edges
    """
    
    def __init__(self):
        self.large  = './data/largeG.txt'
        self.medium = './data/mediumG.txt'
        self.tiny  = './data/tinyG.txt'


    def load_data(self, path):
        """load the specified graph data
        
        # Arguements
            path: path of the data to be loaded
            
        # Returns
            dictionary of graph data.
            data = {'num_nodes' : num_nodes, \
                    'num_edges' : num_edges, \
                    'edges' : edges}
        """
        with open(path) as fl:
            for i, line in enumerate(fl):
                if i == 0:
                    num_nodes = int(line)
                elif i == 1:
                    num_edges = int(line)
                else:
                    break
            edges = [(int(line.split(' ')[0]), \
                      int(line.split(' ')[1].replace('\n',''))) \
                      for line in fl if len(line.split(' ')) == 2]
            data = {'num_nodes' : num_nodes, \
                    'num_edges' : num_edges, \
                    'edges' : edges}
        return data


class GraphPlot:
    """class to visualize the considered graph"""
    
    def __init__(self, num_nodes=0):
        self.num_nodes = num_nodes
        self.node_coords = None
        
    
    def set_num_nodes(self, num_nodes):
        ''' this method sets num_nodes'''
        self.num_nodes = num_nodes
        
    
    def get_num_nodes(self, num_nodes):
        ''' this method returns nodes_coordinates'''
        return self.num_nodes
        
    
    def set_nodes_coordinates(self, node_coords):
        ''' this method sets nodes_coordinates'''
        self.node_coords = node_coords
        
    
    def get_nodes_coordinates(self, node_coords):
        ''' this method returns nodes_coordinates'''
        return self.node_coords

        
    def nodes_coordinates_sun(self):
        """place nodes on a circumference
        
        # Arguements
            num_nodes: number of nodes.
            
        # Returns
            None. it sets self.node_coords.
        """
        angs = np.linspace(0, 2 * np.pi, self.num_nodes + 1)
        angs += 0.5 * np.pi # to start from the top
        xs = np.cos(angs[:-1])
        ys = np.sin(angs[:-1])
        node_coords = np.vstack((xs, ys))
        self.set_nodes_coordinates(node_coords)
    

    def nodes_coordinates_spiral(self, num_layers):
        """place nodes on a circumference but over n layers
           which looks like a spiral
        
        # Arguements
            num_nodes: number of nodes.
            num_layers: number of layers.
            
        # Returns
            None. it sets self.node_coords.
        """
        nd_perlayer = self.num_nodes // num_layers
        # this shift generates the spiral shape 6 can be replaced
        # with an arbitrary number.
        shift = 6 * np.pi
        shift /= nd_perlayer + 1
        shift /= num_layers + 1
        idx_layer = np.arange(1, num_layers + 2)
        idx_layer = np.kron(idx_layer, np.ones(nd_perlayer))
        angs = np.linspace(0, 2 * np.pi, nd_perlayer + 1)[:-1]
        angs += 0.5 * np.pi # to start from the top
        angs = np.kron(np.ones(num_layers + 1), angs)
        angs += idx_layer * shift
        xs = np.cos(angs)
        ys = np.sin(angs)
        node_coords = np.vstack((xs, ys))
        node_coords *= idx_layer
        node_coords = node_coords[:, :self.num_nodes]
        self.set_nodes_coordinates(node_coords)


    def plot_graph(self, edges, label=False):
        """plot the graph for a visualization. coordinates of the 
           nodes should be generated with methods above
        
        # Arguements
            edges: edges of the graph
            num_nodes: number of nodes.
            
        # Returns
            plot of the nodes and edges.
        """
        plt.figure(123, figsize=(6, 8))
        plt.clf()
        if label:
            for i in range(self.node_coords.shape[1]):
                ndx = self.node_coords[0, i]
                ndy = self.node_coords[1, i]
                plt.text(ndx, ndy, '{}'.format(i), fontsize=16)
        for edge in edges:
            edx = [self.node_coords[0, edge[0]], self.node_coords[0, edge[1]]]
            edy = [self.node_coords[1, edge[0]], self.node_coords[1, edge[1]]]
            plt.plot(edx, edy, '-', color=(0.0, 0.4, 0.8), lw=0.05)
        xs = self.node_coords[0]
        ys = self.node_coords[1]
        plt.plot(xs, ys, 'o', color=(0., 0.8, 0.2), markersize=2.)
        plt.xticks([])
        plt.yticks([])


    def plot_path(self, edges, path):
        """plot (the shortest) path between start and target
        
        # Arguements
            edges: edges of the graph.
            path: path to be plotted.
            
        # Returns
            plot of the path with start (red), mids (purple), target(blue)
        """
        plt.figure(123, figsize=(6, 8))
        for i in range(len(path) - 1):
            r = self.node_coords[:, [path[i], path[i+1]]]
            plt.plot(r[0], r[1], '-', color=(0.0, 0.4, 0.8), lw=2.0)
            plt.plot(r[0, 0], r[1, 0], 'o', markersize=4.0\
                                          , color=(0.8, 0., 0.8))
            plt.text(r[0, 0], r[1, 0], '{}'.format(path[i]), fontsize=16)
        # start node
        r = self.node_coords[:, path[0]]
        plt.plot(r[0], r[1], 'ro', markersize=6.0)
        # target node
        r = self.node_coords[:, path[-1]]
        plt.plot(r[0], r[1], 'bo', markersize=6.0)
        plt.text(r[0], r[1], '{}'.format(path[-1]), fontsize=16)
        

if __name__== '__main__':
    print('main')
else:
    print('"loaded graph module"')
    
        