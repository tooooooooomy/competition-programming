a, b = map(int, input().split())

ans = 1
for i in range(1, b+1):
  cnt = b // i - (a-1) // i
  if cnt >= 2:
    ans = i
    
print(ans)
