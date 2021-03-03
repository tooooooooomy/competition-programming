n = int(input())
t = list(map(int, input().split()))
m = int(input())
P, X = [], []

for i in range(m):
  p, x = map(int, input().split())
  P.append(p)
  X.append(x)

s = 0
dic = {}

for i in range(n):
  s += t[i]
  dic[i] = t[i]

for i in range(m):
  k = dic[P[i]-1]
  print(s-k+X[i])
