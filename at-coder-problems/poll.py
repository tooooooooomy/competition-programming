n = int(input())
S = [input() for _ in range(n)]

dic = {}
for s in S:
  if s in dic:
    dic[s] += 1
  else:
    dic[s] = 1
    
s = set()
for k in dic:
    s.add((dic[k], k))

s = sorted(s, reverse=True)

t = s[0][0]
arr = set()
for v, k in s:
    if t == v:
        arr.add(k)
    else:
        break

arr = sorted(arr)
for k in arr:
    print(k)
