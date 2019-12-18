#!/usr/bin/env python
# coding:utf-8

# Dijkstra's algorithm for shortest paths
# David Eppstein, UC Irvine, 4 April 2002
# code source:http://www.algolist.com/code/python/Dijkstra%27s_algorithm

from priodict import priorityDictionary


def Dijkstra(G, start, end=None):
    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary()  # est.dist. of non-final vert.
    Q[start] = 0

    for v in Q:
        D[v] = Q[v]

        if v == end: break

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError, "Dijkstra: found better path to already-final vertex"

                elif w not in Q or vwLength < Q[w]:
                    Q[w] = vwLength
                    P[w] = v

        return (D, P)


def shortestPath(G, start, end):
    D, P = Dijkstra(G, start, end)
    Path = []
    while 1:

        Path.append(end)
        if end == start: break
        end = P[end]

    Path.reverse()
    return Path