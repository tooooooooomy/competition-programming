n, k, q = map(int, input().split())
A = [int(input()) for _ in range(q)]

dic = {}
for a in A:
  if a in dic:
      dic[a] += 1
  else:
      dic[a] = 1

for i in range(n):
  a = 0
  if i+1 in dic:
    a = dic[i+1]

  v = k + a - q

  if v > 0:
    print('Yes')
  else:
    print('No')
