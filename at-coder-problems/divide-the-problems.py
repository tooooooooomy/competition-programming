n = int(input())
d = list(map(int, input().split()))

d.sort()

if n % 2 == 1:
    print(0)
    exit()

m = n // 2

mi = d[m-1] + 1
mx = d[m]

a = 0
while mi <= mx:
    a += 1
    mi += 1

print(a)
