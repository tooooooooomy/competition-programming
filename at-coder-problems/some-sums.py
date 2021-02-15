import math

n, a, b = map(int, input().split())

ans = 0
for i in range(1, n+1):
    l = int(math.log10(i) + 1)
    t = 0
    j = i
    while 0 < l:
        t += j // 10 ** (l-1)
        j %= 10 ** (l-1)
        l -= 1
    if a <= t <= b:
        ans += i

print(ans)
