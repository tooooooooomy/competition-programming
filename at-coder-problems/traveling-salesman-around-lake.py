k, n = map(int, input().split())
a = list(map(int, input().split()))

kukan = []
for i in range(1, n):
    kukan.append(a[i] - a[i-1])

kukan.append(k + a[0] - a[n-1])

kukan.sort()

s = 0
for i in range(len(kukan) - 1):
    s += kukan[i]

print(s)
