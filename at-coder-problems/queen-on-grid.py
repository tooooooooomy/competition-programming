import numpy

def solve(h, w, s):
    dp = numpy.zeros((h, w))
    x = numpy.zeros((h, w))
    y = numpy.zeros((h, w))
    z = numpy.zeros((h, w))
    dp[0, 0] = 1

    mod = 10 ** 9 + 7

    for i in range(h):
        for j in range(w):
            if i == 0 and j == 0:
                continue
            if not s[i][j]:
                continue

            if j > 0:
                x[i, j] = (x[i, j-1] + dp[i, j-1]) % mod

            if i > 0:
                y[i, j] = (y[i-1, j] + dp[i-1, j]) % mod

            if i > 0 and j > 0:
                z[i, j] = (z[i-1, j-1] + dp[i-1, j-1]) % mod

            print(x[i, j] + y[i, j] + z[i, j])
            print(x[i, j],y[i, j], z[i, j])
            dp[i, j] = (x[i, j] + y[i, j] + z[i, j]) % mod

    print(x, y, z)
    return int(dp[h-1, w-1])

h, w = map(int, input().split())
s = [input() for _ in range(h)]
s = [[s[i][j] == '.' for j in range(w)] for i in range(h)]
s = numpy.asarray(s, dtype=bool)
print(solve(h, w, s))

