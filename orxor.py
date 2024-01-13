n = int(input())
a = list(map(int, input().split()))
 
import sys
ans = sys.maxsize
 
for i in range(1 << (n-1)):
  x = 0
  c = 0
  for j in range(n):
    c |= a[j]

    if i >> j & 1:
      x ^= c
      c = 0

  x ^= c
  ans = min(ans, x)
 
print(ans)

