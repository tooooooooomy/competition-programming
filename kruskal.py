es = [
    {'u': 0, 'v': 2, 'cost': 1 },
    {'u': 1, 'v': 2, 'cost': 2 },
    {'u': 1, 'v': 4, 'cost': 10 },
    {'u': 2, 'v': 3, 'cost': 3 },
    {'u': 2, 'v': 5, 'cost': 7 },
    {'u': 3, 'v': 5, 'cost': 1 },
    {'u': 3, 'v': 6,'cost': 5 },
    {'u': 4, 'v': 5, 'cost': 5 },
    {'u': 5, 'v': 6, 'cost': 8 },
]

V = 7
E = 9

def comp(e):
    return e['cost']

def kruskal():
    sorted_es = sorted(es, key=comp)
    init_union_find(V)
    res = 0
    for i in range(E):
        e = sorted_es[i]
        if not same(e['u'], e['v']):
            unite(e['u'], e['v'])
            res += e['cost']

    return res

par = [None] * 1000
rank = [None] * 1000

def init_union_find(n):
    for i in range(n):
        par[i] = i
        rank[i] = 0

def unite(x, y):
    x = find(x)
    y = find(y)

    # find route
    if x == y:
        return

    if rank[x] < rank[y]:
        par[x] = y
    else:
        par[y] = x
        
        if rank[x] == rank[y]:
            rank[x] += 1

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

def same(x, y):
    return find(x) == find(y)

print(kruskal())
