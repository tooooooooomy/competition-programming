n, d = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(n)]
 
ans = 0
for i in range(n-1):
  for j in range(1, n):
    if i >= j:
      continue
    a = 0
    for k in range(d):
      a += (X[i][k] - X[j][k]) ** 2

    b = int(a **.5)
    if abs(b * b - a) < 1e-6:
      ans += 1


print(ans)
