n = 4
m = 3
M = 10000

dp = [[0] * (n+1) for i in range(m+1)]
dp[0][0] = 1

for i in range(1, m+1):
    for j in range(n+1):
        if j - i >= 0:
            dp[i][j] = (dp[i-1][j] + dp[i][j-i]) % M
        else:
            dp[i][j] = dp[i-1][j]


print(dp[m][n])

dp = [[0] * (m+1) for i in range(n+1)]
dp[0][0] = 1

for i in range(n+1):
    for j in range(1, m+1):
        if i - j >= 0:
            dp[i][j] = dp[i][j - 1] + dp[i-j][j]
        else:
            dp[i][j] = dp[i][j - 1]

print(dp[n][m])

