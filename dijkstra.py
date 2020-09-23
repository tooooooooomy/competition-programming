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

def dijkstra(s):
    d[s] = 0

    while True:
        v = -1
        for u in range(V):
            if not used[u] and (v == -1 or d[u] < d[v]):
                v = u

        if v == -1:
            break

        used[v] = True

        for u in range(V):
            d[u] = min(d[u], d[v] + cost[v][u])

dijkstra(0)
print(d)

d = [9999] * V
queue = []

G = [
  [{ 'to': 0, 'cost': 0 }, { 'to': 1, 'cost': 2 }, { 'to': 2, 'cost': 5 }],
  [{ 'to': 0, 'cost': 2 }, { 'to': 1, 'cost': 0 }, { 'to': 2, 'cost': 4 }, { 'to': 3, 'cost': 6 }, { 'to': 4, 'cost': 10 }],
  [{ 'to': 0, 'cost': 5 }, { 'to': 1, 'cost': 4 }, { 'to': 2, 'cost': 0 }, { 'to': 3, 'cost': 2 }],
  [{ 'to': 1, 'cost': 6 }, { 'to': 2, 'cost': 2 }, { 'to': 3, 'cost': 0 },{ 'to': 5, 'cost': 1 }],
  [{ 'to': 1, 'cost': 10 }, { 'to': 4, 'cost': 0 }, { 'to': 5, 'cost': 3 }, { 'to': 6, 'cost': 5 }],
  [{ 'to': 3, 'cost': 1 }, { 'to': 4, 'cost': 3 }, { 'to': 5, 'cost': 0 }, { 'to': 6, 'cost': 9 }],
  [{ 'to': 4, 'cost': 5 }, { 'to': 5, 'cost': 9 }, { 'to': 6, 'cost': 0 }],

]

def dijkstra2(s):
    d[s] = 0
    heapq.heappush(queue, (0, s))

    while not len(queue) is 0:
        p = heapq.heappop(queue)

        v = p[1]
        if d[v] < p[0]:
            continue

        for i in range(len(G[v])):
            e = G[v][i]
            if d[e['to']] > d[v] + e['cost']:
                d[e['to']] = d[v] + e['cost']
                heapq.heappush(queue, (d[e['to']], e['to']))


dijkstra2(0)
print(d)
