n, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

ans = 0
for i in range(n):
    x -= a[i]

    if x < 0:
        break

    ans += 1

if x > 0:
    ans -= 1

print(ans)
