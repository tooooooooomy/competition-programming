n = int(input())
A = list(map(int, input().split()))

m = 1
for a in A:
  m *= a
  
m -= 1
ans = 0
for a in A:
  ans += m % a
  
print(ans)
