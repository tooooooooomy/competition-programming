n = int(input())
A, B = [], []

for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

import sys
ma = sys.maxsize
mb = sys.maxsize
ai, bi = -1, -1

for i in range(n):
    if A[i] < ma:
        ai = i
        ma = A[i]
    if B[i] < mb:
        bi = i
        mb = B[i]

if ai != bi:
    print(max(ma, mb))
    exit()

sa = sorted(A)
sb = sorted(B)

print(min(min(max(sa[0], sb[1]), max(sa[1], sb[0])), mb+ma))
