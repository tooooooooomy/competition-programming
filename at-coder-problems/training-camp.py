n = int(input())

a = 1
for i in range(1, n+1):
  if a > (10 ** 9 + 7):
      a %= (10 ** 9 + 7)
  a *= i

print(a % (10 ** 9 + 7))
