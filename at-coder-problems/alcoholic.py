N, X = map(int, input().split())
V, P = [], []
c = 0
ans = 0
for i in range(N):
    v, p = map(int, input().split())

    V.append(v)
    P.append(p)

for i in range(N):
    if c > X * 100:
        break

    c += V[i] * P[i]
    if P[i] != 0:
        ans += 1

if int(c) <= X * 100:
    print(-1)
else:
    print(ans)
