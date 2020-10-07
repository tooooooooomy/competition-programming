import sys

par = [None] * 1000
rank = [None] * 1000

def init(n):
    for i in range(n):
        par[i] = i
        rank[i] = 0

def find(x):
    if par[x] == x:
        return x
    else:
        par[x] = find(par[x])
        return par[x]

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

def same(x, y):
    return find(x) == find(y)

N = 100
K = 7
T = [1, 2, 2, 2, 1, 2, 1]
X = [101, 1, 2, 3, 1, 3, 5]
Y = [1, 2, 3, 3, 3, 1, 5]

def solve():
    init(N*3)
    ans = 0
    for i in range(K):
        t = T[i]
        x = X[i] - 1
        y = Y[i] - 1

        if x < 0 or N <= x or y < 0 or N <= y:
            ans += 1
            continue

        if t == 1:
            if same(x, y + N) or same(x, y + 2 * N):
                ans += 1
            else:
                unite(x, y)
                unite(x, y + N)
                unite(x, y + 2 * N)
        else:
            if same(x, y) or same(x, y + 2 * N):
                ans += 1
            else:
                unite(x, y + N)
                unite(x + N, y + 2 * N)
                unite(x + 2 * N, y)

    print(ans)

solve()
