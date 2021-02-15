h, w = map(int, input().split())
s = [input() for _ in range(h)]
 
ans = 0
for i in range(h-1):
  for j in range(w-1):
    cnt = 0
    for di in range(i, i+2):
      for dj in range(j, j+2):
        if s[di][dj] == '#':
          cnt += 1
    if cnt == 1 or cnt == 3:
      ans += 1

print(ans)
