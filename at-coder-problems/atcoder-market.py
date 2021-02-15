def solve(n, a, b):
    a = sorted(a)
    b = sorted(b)

    s_i = len(a) // 2
    g_i = len(b) // 2

    ans = 0
    for i in range(n):
        if s_i > i:
            ans += a[s_i] - a[i]
        else:
            ans += a[i] - a[s_i]

        ans += b[i] - a[i]

        if g_i < i:
            ans += b[i] - b[g_i]
        else:
            ans += b[g_i] - b[i]

    return ans


n = int(input())
a, b = [], []
for i in range(n):
    p1, p2 = map(int, input().split())
    a.append(p1)
    b.append(p2)

print(solve(n, a, b))
