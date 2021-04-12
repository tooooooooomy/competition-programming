n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: x[0])

ans = 0
i = 0
for a, b in arr:
  if i + b >= m:
    ans += a * (m-i)
    break
  ans += a * b
  i += b
  
print(ans)
