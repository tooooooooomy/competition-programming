n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

import sys
ans = sys.maxsize
 
for i in range(n):
  a, p, x = arr[i]
  
  if (x - a > 0):
    ans = min(ans, p)
    
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
