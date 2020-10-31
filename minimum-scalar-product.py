def solve(n, v1, v2):
    v1 = sorted(v1)
    v2 = sorted(v2, reverse=True)
    print(v1)
    print(v2)

    res = 0
    for i in range(n):
        res += v1[i] * v2[i]

    return res


n = 3
v1 = [1, 3, -5]
v2 = [-2, 4, 1]

print(solve(n, v1, v2))

n = 5
v1 = [1, 2, 3, 4, 5]
v2 = [1, 0, 1, 0, 1]

print(solve(n, v1, v2))

