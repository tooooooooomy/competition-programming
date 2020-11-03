def solve(N, K, L):
    sorted_l = sorted(L, reverse=True)
    a = 0
    for i in range(K):
        a += sorted_l[i]

    return a

print(solve(5, 3, [1, 2, 3, 4, 5]) == 12)
print(solve(15, 14, [50, 26, 27, 21, 41, 7, 42, 35, 7, 5, 5, 36, 39, 1, 45]) == 386)
