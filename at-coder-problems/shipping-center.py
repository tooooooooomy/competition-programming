n, m, q = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(n)]

x = list(map(int, input().split()))
X = []
for i in range(m):
    X.append((x[i], i+1))
X.sort()

qs = [list(map(int, input().split())) for _ in range(q)]

ans = [0] * q
for i in range(q):
    l, r = qs[i]
    used = [False] * n
    tbags = bags
    tbags.sort(key=lambda x: x[1], reverse=True)
    for k in range(m):
        if l <= X[k][1] <= r:
            continue

        for j in range(n):
            w, v = tbags[j]
            if used[j]:
                continue

            if w <= X[k][0]:
                if i == 2:
                    print(w, v)
                ans[i] += v
                used[j] = True
                break

for a in ans:
    print(a)
