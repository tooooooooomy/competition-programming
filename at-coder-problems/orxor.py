n = int(input())
a = list(map(int, input().split()))

import sys
ans = sys.maxsize

for s in range(1<<(n-1)):
    now = 0
    o = 0
    for i in range(n):
        o |= a[i]
        if (s>>i&1):
            now ^= o
            o = 0

    now ^= o
    ans = min(ans, now)

print(ans)
