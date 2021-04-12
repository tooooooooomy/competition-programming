n = int(input())
A = list(map(int, input().split()))

ans = 3 ** n
two = 0
for a in A:
  if a % 2 == 0:
      two += 1

if two == 0:
    print(ans - 1)
else:
    print(ans - 2 ** two)
