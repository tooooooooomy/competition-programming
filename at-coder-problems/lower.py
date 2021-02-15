n = int(input())
H = list(map(int, input().split()))
 
t_a = 0
ans = 0
m = H[0]
for i in range(1, len(H)):
  if m >= H[i]:
    t_a += 1
    ans = max(ans, t_a)
  else:
    t_a = 0
  m = H[i]
 
print(ans)
