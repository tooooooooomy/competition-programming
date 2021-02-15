import sys

n = int(input())
x = list(map(int, input().split()))

r = x[0]
l = x[0]

for i in range(n):
    l = min(l, x[i])
    r = max(r, x[i])

ans = sys.maxsize

for i in range(l, r+1):
    cost = 0
    for j in range(n):
        cost += (x[j] - i) ** 2
    ans = min(ans, cost)

print(ans)
