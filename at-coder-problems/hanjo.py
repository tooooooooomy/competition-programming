h,w,a,b = map(int, input().split())

used = [[False] * 16 for _ in range(16)]

def dfs(i, j, a, b):
  if a < 0 or b < 0:
    return 0
  if j == w:
    j = 0
    i += 1
  if i == h:
    return 1
  if used[i][j]:
    return dfs(i, j+1, a, b)
  
  used[i][j] = True
  res = 0
  res += dfs(i, j, a, b-1)
  if j+1 < w and not used[i][j+1]:
    used[i][j+1] = True
    res += dfs(i, j+1, a-1, b)
    used[i][j+1] = False
  if i+1 < h and not used[i+1][j]:
    used[i+1][j] = True
    res += dfs(i, j+1, a-1, b)
    used[i+1][j] = False
  
  used[i][j] = False
  
  return res
  
print(dfs(0, 0, a, b))
