# -*- coding: utf-8 -*-

import heapq

cost = [
  [0, 2, 5, 9999, 9999, 9999, 9999],
  [2, 0, 4, 6, 10, 9999, 9999],
  [5, 4, 0, 2, 9999, 9999, 9999],
  [9999, 6, 2, 0, 9999, 1, 9999],
  [9999, 10, 9999, 9999, 0, 3, 5],
  [9999, 9999, 9999, 1, 3, 0, 9],
  [9999, 9999, 9999, 9999, 5, 9, 0],
]

V = 7
d = [9999] * V
used = [False] * V
prev = [-1] * V

def dijkstra(s):
    d[s] = 0

    while True:
        v = -1
        for u in range(V):
            # 使われていない頂点のうち距離が最小のものを探す
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u

        if v == -1:
            break
        used[v] = True

        for u in range(V):
            if d[u] > d[v] + cost[v][u]:
                d[u] = d[v] + cost[v][u]
                prev[u] = v

dijkstra(2)

def get_path(t):
    path = []
    path.append(t)

    while True:
        t = prev[t]

        if t == -1:
            break

        path.append(t)
    
    return path[::-1]

path = get_path(5)
print(path)

