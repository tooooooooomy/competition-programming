cost = [
    [0, 9999, 1, 9999, 9999, 9999, 9999],
    [9999, 0, 2, 9999, 10, 9999, 9999],
    [1, 2, 0, 3, 9999, 7, 9999],
    [9999, 9999, 3, 0, 9999, 1, 5],
    [9999, 10, 9999, 9999, 0, 5, 9999],
    [9999, 9999, 7, 1, 5, 0, 8],
    [9999, 9999, 9999, 5, 9999, 8, 0],
]
V = 7
mincost = [9999] * V
mincost[0] = 0
used = [False] * V

def prim():
    res = 0
    
    while(True):
        v = -1
        for u in range(V):
            if not used[u] and (v == -1 or mincost[u] < mincost[v]):
                v = u


        if v == -1:
            break
        used[v] = True
        res += mincost[v]

        for u in range(V):
            mincost[u] = min(mincost[u], cost[v][u])

    return res


print(prim())
