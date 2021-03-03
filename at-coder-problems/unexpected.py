n = int(input())
 
s = set()
sq = int(n **.5)
for i in range(2, sq+1):
    x = i * i
    while x <= n:
        s.add(x)
        x *= i

print(n-len(s))
