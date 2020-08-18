n = 5
a = [4, 2, 3, 1, 5]
dp = [1] * n
res = 0

for i in range(n):
    for j in range(i):
        if a[j] < a[i]: 
            dp[i] = max(dp[i], dp[j] + 1)

    res = max(res, dp[i])

print(res)
