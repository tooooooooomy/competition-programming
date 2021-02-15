from decimal import Decimal
x, y, r = map(Decimal, input().split())

x, y, r = x*10000, y*10000, r*10000
x %= 10000
y %= 10000

def inside(dx, dy, z):
    return dx ** 2 + dy ** 2 <= z ** 2

def solve(x, y, z, lim):
    l, r = 0, 1
    res = 0
    i = 10 ** 9 + 50000
    while i >= lim:
        while inside(x-l*10000, i-y, z):
            l -= 1
        while inside(r*10000-x, i-y, z):
            r += 1

        res += r-l-1
        i -= 10000

    return res

ans = solve(x, y, r, 10000)
ans += solve(x, -y, r, 0)

print(ans)
