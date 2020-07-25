N = 6
R = 10
X = [1, 7, 15, 20, 30, 50]

def solve(N, R, X):
    i = 0
    ans = 0
    while i < N:
        # カバーされていない一番左の点
        s = X[i]
        i += 1

        while i < N and X[i] <= s + R:
            i += 1

        # 印をつける予定の点
        p = X[i-1]
        
        while i < N and X[i] <= p + R:
            i += 1

        ans += 1

    return ans

print(solve(N, R, X))

