import heapq

N = 4
R = 4
dist = [9999] * 99
dist2 = [9999] * 99
que = []
G = [
    [ { 'to': 0, 'cost': 0 }, { 'to': 1, 'cost': 100 }, { 'to': 2, 'cost': 9999 }, { 'to': 3, 'cost': 9999 }  ],
    [ { 'to': 0, 'cost': 100 }, { 'to': 1, 'cost': 0 }, { 'to': 2, 'cost': 250 }, { 'to': 3, 'cost': 200 }  ],
    [ { 'to': 0, 'cost': 9999 }, { 'to': 1, 'cost': 250 }, { 'to': 2, 'cost': 0 }, { 'to': 3, 'cost': 100 }  ],
    [ { 'to': 0, 'cost': 9999 }, { 'to': 1, 'cost': 200 }, { 'to': 2, 'cost': 100 }, { 'to': 3, 'cost': 0 }  ],
]

def solve():
    dist[0] = 0
    # first distance, second vertex
    heapq.heappush(que, (0, 0))

    while(que):
        p = heapq.heappop(que)
        v = p[1]
        d = p[0]
        if dist2[v] < d:
            continue

        for i in range(N):
            e = G[v][i]
            d2 = d + e['cost']
            if dist[e['to']] > d2:
                # point! swap
                tmp = dist[e['to']]
                dist[e['to']] = d2
                d2 = tmp
                heapq.heappush(que, (dist[e['to']], e['to']))

            if dist2[e['to']] > d2 and dist[e['to']] < d2:
                dist2[e['to']] = d2
                heapq.heappush(que, (dist2[e['to']], e['to']))


    print(dist2[N-1])

solve()
