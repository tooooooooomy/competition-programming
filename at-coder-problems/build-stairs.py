n = int(input())
h = list(map(int, input().split()))


if n == 1:
  print('Yes')
  exit()

for i in range(1, n):
  if h[i-1] < h[i]:
    h[i] -= 1
  

  if h[i-1] > h[i]:
    print('No')
    exit()
    
print('Yes')
