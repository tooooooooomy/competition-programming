n = int(input())

if n == 1:
    print(1)
    exit()

a = 0

sqr = int(n **.5)

for i in range(2, sqr+1):
  j = 2
  while i ** j <= n:
    a = max(a, i ** j)
    j += 1
    
print(a)
