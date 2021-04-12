a, b, c = map(int, input().split())

m = a * b * c

if a % 2 == 0 or b % 2 == 0 or c % 2 == 0:
  print(0)
else:
  print(min((a//2+1)*b*c, (b//2+1)*a*c, (c//2+1)*a*b) - max((a//2)*b*c, (b//2)*a*c, (c//2)*a*b))
