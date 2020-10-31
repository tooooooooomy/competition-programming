def solve(M, P, X):
    n = 1 << M
    dp = [[0.0] * (1 << M + 1) for i in range(2)]

    prv = dp[0]
    nxt = dp[1]
    prv[n] = 1.0

    for r in range(M):
        for i in range(n+1):
            jub = min(i, n-1)
            t = 0.0
            for j in range(jub+1):
                t = max(t, P * prv[i+j] + (1 - P) * prv[i - j])

            nxt[i] = t

        prv, nxt = nxt, prv

    i = X * n / 1000000
    print(prv[i])




M = 1
P = 0.5
X = 500000
solve(M, P, X)

M = 3
P = 0.75
X = 600000
solve(M, P, X)
