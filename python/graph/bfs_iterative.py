#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import graph as G


def bfs_traversal_iterative(grph, s):
    """traverse the graph via iterative bfs
        
    # Arguements
        gg: graph.
        s: start node.
            
    # Returns
        None. The graph has been traversed and processed
    """
    grph.nds[s].set_distance(0)
    que = G.Queue()
    que.enqueue(s)
    while not que.isEmpty():
        curr = que.dequeue()
        for nbr in grph.nds[curr].get_neighbors():
            if grph.nds[nbr].get_visit() == 0:
                grph.nds[nbr].set_visit(0.5)
                #could be just 1. 0.5 means found but not stepped yet.
                grph.nds[nbr].set_distance(grph.nds[curr].get_distance() + 1)
                grph.nds[nbr].set_prev(curr)
                que.enqueue(nbr)
        grph.nds[curr].set_visit(1)


def bfs_shortest_path_iterative(grph, s, t):
    """find the shortest path between s and t via iterative bfs
        
    # Arguements
        gg: graph.
        s: start node.
        t: target node.
            
    # Returns
        the shotest distance and the path
        if s and t are not connected, returns inf and None respectively.
    """
    grph.nds[s].set_distance(0)
    que = G.Queue()
    que.enqueue(s)
    while not que.isEmpty():
        curr = que.dequeue()
        if curr == t:
            return grph.nds[curr].get_distance(), grph.retrieve_path(curr)
        for nbr in grph.nds[curr].get_neighbors():
            if grph.nds[nbr].get_visit() == 0:
                grph.nds[nbr].set_visit(0.5)
                #could be just 1. 0.5 means found but not stepped yet.
                grph.nds[nbr].set_distance(grph.nds[curr].get_distance() + 1)
                grph.nds[nbr].set_prev(curr)
                que.enqueue(nbr)
            grph.nds[curr].set_visit(1)
    return 'inf', None


def main():
    """find the shortest path between start and target via iterative bfs
        
    # Arguements.
            
    # Returns
        the shotest distance and the path
        if s and t are not connected, returns inf and None respectively.
    """
    start = 1
    target = 205
    data = G.GraphData()
    data = data.load_data(data.medium)
    grph = G.UndirectedGraph(data['edges'])
    myplt = G.GraphPlot(data['num_nodes'])
    myplt.nodes_coordinates_spiral(25)
    myplt.plot_graph(data['edges'])
    dist, path = bfs_shortest_path_iterative(grph, start, target)
    if path is not None:
        myplt.plot_path(data['edges'], path)
    print('shortest path distance : ', dist)
    print('shortest path          : ', path)


if __name__ == '__main__':
    main()