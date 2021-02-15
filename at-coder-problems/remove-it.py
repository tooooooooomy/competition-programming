n, x = map(int, input().split())
A = list(map(int, input().split()))
 
new_a = []
 
for a in A:
  if a is not x:
    new_a.append(str(a))
    
print(" ".join(new_a))
