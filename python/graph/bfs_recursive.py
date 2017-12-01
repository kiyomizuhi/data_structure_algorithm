#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import graph as G
import sys


def bfs_traversal_recursive(grph, que, s):
    """traverse the graph via recursive bfs
        
    # Arguements
        grph: graph.
        que: queue for bfs.
        s: start node.
            
    # Returns
        recursive bfs.
    """
    if que.isEmpty():
        return
    curr = que.dequeue()
    for nbr in grph.nds[curr].get_neighbors():
        if grph.nds[nbr].get_visit() == 0:
            grph.nds[nbr].set_visit(0.5)
            grph.nds[nbr].set_distance(grph.nds[curr].get_distance() + 1)
            grph.nds[nbr].set_prev(curr)
            que.enqueue(nbr)
    grph.nds[curr].set_visit(1)
    bfs_traversal_recursive(grph, que, curr)


def bfs_shortest_path_recursive(grph, que, s, t):
    """find the shortest path between s and t via iterative bfs
        
    # Arguements
        grph: graph.
        que: queue for bfs.
        s: start node.
        t: target node.
            
    # Returns
        recursive bfs shortest path.
    """
    if que.isEmpty() or s == t:
        return
    curr = que.dequeue()
    for nbr in grph.nds[curr].get_neighbors():
        if grph.nds[nbr].get_visit() == 0:
            grph.nds[nbr].set_visit(0.5)
            grph.nds[nbr].set_distance(grph.nds[curr].get_distance() + 1)
            grph.nds[nbr].set_prev(curr)
            que.enqueue(nbr)
    grph.nds[curr].set_visit(1)
    bfs_shortest_path_recursive(grph, que, curr, t)


def main():
    """find the shortest path between start and target via iterative bfs
        
    # Arguements.
            
    # Returns
        the shotest distance and the path
        if s and t are not connected, returns inf and None respectively.
    """
    start = 1
    target = 125
    data = G.GraphData()
    data = data.load_data(data.medium)
    grph = G.UndirectedGraph(data['edges'])
    myplt = G.GraphPlot(data['num_nodes'])
    myplt.nodes_coordinates_spiral(25)
    myplt.plot_graph(data['edges'])
    que = G.Queue()
    que.enqueue(start)
    grph.nds[start].set_distance(0)
    bfs_shortest_path_recursive(grph, que, start, target)
    dist = grph.nds[target].get_distance()
    if dist != sys.maxsize:
        path = grph.retrieve_path(target)
        myplt.plot_path(data['edges'], path)
    print('shortest path distance : ', dist)
    print('shortest path          : ', path)


if __name__ == '__main__':
    main()
