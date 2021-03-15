n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    if i > 0:
        dp[i] += dp[i-1]

    dp[i] += min(a[i], b[i])
    c = max(b[i] - a[i], 0)
    dp[i] += min(a[i+1], c)
    a[i+1] = max(a[i+1] - c, 0)

print(dp[n-1])
