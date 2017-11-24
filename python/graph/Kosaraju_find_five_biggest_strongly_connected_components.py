# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 17:21:51 2017

@author: Hiro
"""
from collections import defaultdict
from heapq import nlargest

class Vertex:
    def __init__(self):
        ''' vertex object'''
        self.visit = 0
        self.neighbours = list()
        self.label = 0
        self.prev_vertex = None


class Graph:
    def __init__(self, edges, nvert):
        ''' graph object'''
        self.vertices = defaultdict(lambda: Vertex())
        self.edges = edges
        self.nvert = nvert #number of vertices
        self.fin_time = [i for i in range(1, nvert+1)]

        for edge in edges:
            self.vertices[edge[0]].neighbours.append(self.vertices[edge[1]])
            self.vertices[edge[0]].label = edge[0]

    def get_unvisited_neighbours(self, label):
        ''' get unvisited neighbors among all the neighbors '''
        unbr = []
        for nbr in self.vertices[label].neighbours:
            if nbr.visit == 0:
                unbr.append(nbr)
        return unbr

    def reversed_graph(self):
        ''' as the name says '''
        return Graph([[edge[1], edge[0]] for edge in self.edges], self.nvert)


def dfs_loop(graph, fin_time):
    ''' dfs loop for both the first and second pass '''
    scc = []
    stack_count = 0
    for node in fin_time[::-1]:
        if graph.vertices[node].visit == 0:
            curr_vertex = graph.vertices[node]

            scc_count = 0
            while curr_vertex is not None:
                curr_vertex.visit = 1
                if graph.get_unvisited_neighbours(curr_vertex.label) == []:
                    graph.fin_time[stack_count] = curr_vertex.label
                    stack_count += 1
                    scc_count += 1

                    next_vertex = curr_vertex.prev_vertex
                    curr_vertex = next_vertex

                else:
                    next_vertex = graph.get_unvisited_neighbours\
                                    (curr_vertex.label)[0]
                    next_vertex.prev_vertex = curr_vertex
                    curr_vertex = next_vertex

            scc.append(scc_count)
    return scc

def main():
    ''' main '''
    #loading the data
    print('\nloading the data')
    location = 'SCC.txt'
    edges = []
    with open(location) as ff:
        for line in ff:
            u, v = line.split()
            edges.append([int(u), int(v)])
    print('--- done ---')

    #starting here
    nnn = 875714

    print('\ngenerating the graph')
    g_normal = Graph(edges, nnn)
    print('--- done ---')

    print('\ngenerating the reversed graph')
    g_reverse = g_normal.reversed_graph()
    print('--- done ---')

    print('\nfirst pass started')
    dfs_loop(g_reverse, g_normal.fin_time)
    print('--- done ---')

    print('\nsecond pass started')
    scc = dfs_loop(g_normal, g_reverse.fin_time)
    print('--- done ---')

    print('\nscc :', nlargest(5, scc))

if __name__ == '__main__':
    main()
