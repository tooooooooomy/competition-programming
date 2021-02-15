import itertools

n, m = map(int, input().split())

k = [0] * m
s = [[]] * m

for i in range(m):
    line = list(map(int, input().split()))
    k[i] = line[0]
    for j in range(k[i]):
        s[i] = line[1:]

p = list(map(int, input().split()))
ans = 0

for i in range(1 << n):
    for j in range(m):
        count = 0
        for k in range(n):
            if ((i >> k) & 1) and k+1 in s[j]:
                count += 1
        if count % 2 != p[j]:
            break
    else:
        ans += 1

print(ans)
