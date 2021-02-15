n, m = map(int, input().split())
L, R = [], []

for i in range(m):
    l, r = map(int, input().split())
    L.append(l)
    R.append(r)

ans = 0
L.sort(reverse=True)
R.sort()

if (R[0] - L[0] < 0):
    print(0)
else:
    print(R[0]-L[0] + 1)
