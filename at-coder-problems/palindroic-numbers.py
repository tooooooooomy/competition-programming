a, b = map(int, input().split())
 
ans = 0
while a <= b:
  s = str(a)
  l = len(s)
  for i in range(l // 2):
    if s[i] != s[l-i-1]:
      i -= 1
      break
  if i == (l // 2)-1:
    ans += 1
  a += 1
  
print(ans)
