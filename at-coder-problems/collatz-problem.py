s = int(input())
 
def f(n):
  if n % 2 == 0:
    return n // 2
  else:
    return 3 * n + 1
  
a = [s]
 
for i in range(1000000):
  n = f(a[i])
  if n in a:
    print(i+2)
    break
  
  a.append(n)
