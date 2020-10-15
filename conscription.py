N = 5
M = 5
R = 8

# the relation of x and y
li = [
  [4, 3, 6831],
  [1, 3, 4583],
  [0, 0, 6592],
  [0, 1, 3063],
  [3, 3, 4975],
  [1, 3, 2049],
  [4, 2, 2104],
  [2, 2, 781],
]
es = [{}] * R
E = R
V = N + M

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

def solve():
    for i in range(R):
        es[i] = { 'u': li[i][0], 'v': N + li[i][1], 'cost': -li[i][2] }

    print(10000 * (N + M) + kruskal())

solve()


