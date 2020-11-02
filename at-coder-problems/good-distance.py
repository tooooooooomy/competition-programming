def solve(N, D, X):
    a = 0
    for i in range(N-1):
        for j in range(1, N):
            if i >= j:
                continue

            su = 0
            for d in range(D):
                su += (X[i][d] - X[j][d]) * (X[i][d] - X[j][d])
            

            b = 1
            while b * b < su:
                b += 1

            if b * b == su:
                a += 1

    return a


print(solve(3, 2, [[1, 2], [5, 5], [-2, 8]]) == 1)
print(solve(3, 4, [[-3, 7, 8, 2], [-12, 1, 10, 2], [-2, 8, 9, 3]]) == 2)
print(solve(5, 1, [[1], [2], [3], [4], [5]]) == 10)
