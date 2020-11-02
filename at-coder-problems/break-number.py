def solve(N):
    if N == 1:
        return 1

    a = 0
    prev_c = 0
    for i in range(2, N+1, 2):
        j = i
        c = 0
        while j > 0:
            j /= 2
            c += 1

        if c > prev_c:
            a = i
            prev_c = c

    return a

print(solve(7) == 4)
print(solve(32) == 32)
print(solve(1) == 1)
print(solve(100) == 64)
