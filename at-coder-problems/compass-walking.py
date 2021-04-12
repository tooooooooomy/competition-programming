r, x, y = map(int, input().split())

import math

ans = 0

k = math.sqrt(x**2 + y**2)

while k > 2*r:
    k -= r
    ans += 1

if k == r:
    ans += 1
else:
    ans += 2

print(ans)
