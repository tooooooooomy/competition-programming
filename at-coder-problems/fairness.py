a,b,c,k = map(int, input().split())
 
i = 0
while i < k:
  a, b, c = b + c, a + c, a + b
  i += 1
 
if a - b > 10 ** 18:
  print('Unfair')
else:
  print(a-b)  
