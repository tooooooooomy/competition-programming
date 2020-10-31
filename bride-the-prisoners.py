# -*- coding: utf-8 -*-

def solve(P, Q, A):
    # 簡単のため, 端を追加する
    A.insert(0, 0)
    A.append(P+1)

    dp = [[0] * (Q+2) for i in range(Q+1)]

    # 幅が小さい順にdpを埋めていく
    for w in range(2, Q+2):
        i = 0
        while i+w < Q+2:
            j = i + w
            t = 9999

            # 最初に解放する囚人をすべて試し、最小コストのものを探す
            for k in range(i+1, j):
                t = min(t, dp[i][k] + dp[k][j])

            # 最初解放では解放する囚人に関わらずA[j] - A[i] - 2の金貨が必要
            dp[i][j] = t + A[j] - A[i] - 2
            print(dp)

            i += 1

    return dp[0][Q+1]

P = 20
Q = 3
A = [3, 6, 14]
print(solve(P, Q, A))
