def solve(N, K):
    a = 0
    while N > 0:
        N /= K
        a += 1

    return a

print(solve(11, 2) == 4)
print(solve(1010101, 10) == 7)
print(solve(314159265, 3) == 18)
