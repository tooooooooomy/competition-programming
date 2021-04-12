n = int(input())
a = list(map(int, input().split()))

import sys
ans = sys.maxsize
s = 0
a_s = sum(a)
for i in range(n):
    s += a[i]
    a_s -= a[i]
    ans = min(ans, abs(s - a_s))

print(ans)
