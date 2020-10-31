def solve(N, M):
    res = 0

    a = [-1] * N
    for i in range(N):
        for j in range(N):
            if M[i][j] == 1:
                a[i] = j

    for i in range(N):
        pos = -1
        for j in range(i, N):
            if a[j] <= i:
                pos = j
                break

        j = pos
        while j > i:
            tmp = a[j]
            a[j] = a[j-1]
            a[j-1] = tmp
            res += 1
            j -= 1

    return res


N = 2
M = [
    [1, 0],
    [1, 1],
]
print(solve(N, M))

N = 3
M = [
    [0, 0, 1],
    [1, 0, 0],
    [0, 1, 0],
]
print(solve(N, M))

N = 4
M = [
    [1, 1, 1, 0],
    [1, 1, 0, 0],
    [1, 1, 0, 0],
    [1, 0, 0, 0],
]
print(solve(N, M))
