#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import graph


edges = [[0, 1]]

class graph_rev(graph.Graph):
    def reverse_graph(self):
        print('kaka')

g = graph_rev(edges).reverse_graph()
