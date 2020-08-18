import sys, bisect

n = 5
a = [4, 2, 3, 1, 5]
dp = [sys.maxsize] * n

for i in range(n):
    dp[bisect.bisect_left(dp, a[i])] = a[i]

print(bisect.bisect_left(dp, sys.maxsize))
