n = int(input())
a = list(map(int, input().split()))

a.sort(reverse=True)

s = 0
for i in range(1, 2 * n, 2):
    s += a[i]

print(s)
