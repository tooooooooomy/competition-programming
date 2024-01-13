n, k = map(int, input().split())

c = list(map(int, input().split()))

dic = {}

ans = 0
l = 0
r = 0
for i in range(n):
  if (r-l+1) > k:
    dic[c[l]] -= 1
    if dic[c[l]] == 0:
      del dic[c[l]]
    l += 1
  if c[i] in dic:
    dic[c[i]] += 1
  else:
    dic[c[i]] = 1
  
  ans = max(ans, len(dic.keys()))
  r += 1
  
print(ans)
