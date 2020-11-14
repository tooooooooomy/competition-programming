def solve(N, C, K, T):
    a = 1
    sorted_t = sorted(T, reverse=True)
    b = sorted_t[0]
    i = 1
    t_l = len(T)
    c = 1
    while i < t_l:
        if c < C and b - sorted_t[i] <= K:
            i += 1
            c += 1
        else:
            b = sorted_t[i]
            i += 1
            a += 1
            c = 1

    return a


N, C, K = map(int, input().split())
T = []
for _ in range(N):
    T.append(int(input()))


print(solve(N, C, K, T))


print(solve(5, 3, 5, [1, 2, 3, 6, 12]) == 3)
print(solve(6, 3, 3, [7, 6, 2, 8, 10, 6]) == 3)
