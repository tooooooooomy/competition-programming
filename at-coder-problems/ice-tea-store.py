q, h, s, d = map(int, input().split())
n = int(input())

n *= 4

ans = 0

if n >= 8:
    ans += (n // 8) * (min(q*8, h*4, s*2, d))
    n -= 8 * (n//8)
if n >= 4:
    ans += (n // 4) * (min(q*4, h*2, s))
    n -= 4 * (n//4)
if n >= 2:
    ans += (n // 2) * (min(q*2, h))
    n -= 2 * (n//2)

ans += n * q

print(ans)
