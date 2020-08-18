n = 4
L = [[2, 3], [1, 2], [3, 4], [2, 2]]
W = 5
dp = [[-1] * (W+1)] * (n+1)

def rec(i, j):
    if dp[i][j] >= 0:
        return dp[i][j]

    res = 0
    if i == n:
        res = 0
    elif j < L[i][0]:
        res = rec(i + 1, j)
    else:
        a = rec(i + 1, j - L[i][0]) + L[i][1]
        b = rec(i + 1, j)
        res = max(a, b)

    dp[i][j] = res

    return res

print(rec(0, W))
