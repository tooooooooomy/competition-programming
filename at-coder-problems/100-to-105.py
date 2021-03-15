n = int(input())

if n < 100:
  print(0)
  exit()

if n % 100 == 0:
  print(1)
  exit()

s = 0
a = 105
while s <= n:
  if a < 100:
    print(0)
    exit()

  if s == n:
    print(1)
    exit()

  if s % 100 == n % 100:
      s += 100
  else:
      while s % 100 + a % 100 > n % 100:
        a -= 1
        
      s += a

print(0)
