n = int(input())
arr = [list(map(str, input().split())) for _ in range(n)]

dic = {}

for i in range(n):
  s, p = arr[i]
  p = int(p)
  
  if s not in dic:
    dic[s] = []
  
  dic[s].append((p, i+1))
    
cities = sorted(dic.keys())

for c in cities:
    rs = sorted(dic[c], reverse=True)
    for r in rs:
        print(r[1])

