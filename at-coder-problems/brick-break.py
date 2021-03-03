n = int(input())
a = list(map(int, input().split()))
 
ans = 0
j = 0
for i in range(n):
  if a[i] == j + 1:
    j += 1
  else:
    ans += 1
    
if ans == n:
    print(-1)
else:
    print(ans)
