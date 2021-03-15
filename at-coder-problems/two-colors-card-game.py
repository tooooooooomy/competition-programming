n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

ndic = {}

for i in range(n):
  if s[i] in ndic:
    ndic[s[i]] += 1
  else:
    ndic[s[i]] = 1
    
for i in range(m):
  if t[i] in ndic:
    ndic[t[i]] = max(0, ndic[t[i]] - 1)

print(max(ndic.values()))
