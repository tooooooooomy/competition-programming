def solve(N, T, A, H):
    a = 0
    prev_d = 9999
    for i in range(N):
        av = T * H[i] * 0.006
        if abs(A - av) < prev_d:
            a = i + 1
            prev_d = abs(A - av)

    return a

print(solve(2, 12, 5, [1000, 2000]) == 1)
print(solve(3, 21, -11, [81234, 94124, 52141]) == 3)

