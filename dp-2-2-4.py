n = 3
a = [3, 5, 8]
m = [3, 2, 2]
K = 17

dp = [-1] * (K+1)
dp[0] = 0

def solve():
    for i in range(n):
        print(i)
        for j in range(K+1):
            if dp[j] >= 0:
                dp[j] = m[i]
            elif j < a[i] or dp[j-a[i]] <= 0:
                dp[j] = -1
            else:
                dp[j] = dp[j-a[i]] - 1

            print(dp)


    if dp[K] >= 0:
        print("Yes\n")
    else:
        print("No\n")

solve()
