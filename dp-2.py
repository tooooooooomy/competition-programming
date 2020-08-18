n = 4
m = 4
s = "abcd"
t = "bcda"
dp = [[0] * (m+1)] * (n+1)

def solve():
    for i in range(n):
        for j in range(m):
            if s[i] == t[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])

    return dp[n][m]

print(solve())
