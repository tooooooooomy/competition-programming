A = int(input())
B = int(input())
C = int(input())
X = int(input())
 
a = 0
b = 0
c = 0
 
ans = 0
while a <= A:
  b = 0
  if 500 * a > X:
    break
    
  while b <= B:
    c = 0
    if 500 * a + 100 * b > X:
    	break
        
    while c <= C:
      s = 500 * a + 100 * b + 50 * c
      if s > X:
        break
      
      if s == X:
        ans += 1
        
      c += 1
    
    b += 1
  a += 1
 
print(ans)
