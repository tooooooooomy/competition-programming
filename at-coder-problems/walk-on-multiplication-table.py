n = int(input())

import sys
ans = sys.maxsize

sqr = int(n **.5)

j = 1
for i in range(1, sqr+1):
    if n % i == 0:
        j = n // i

    if i * j == n:
        ans = min(ans, i-1+j-1)


print(ans)
