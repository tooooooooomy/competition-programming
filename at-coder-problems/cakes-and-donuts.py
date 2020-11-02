def solve(N):
    d_4 = N / 4
    d_7 = N / 7

    for i in range(d_4 + 1):
        for j in range(d_7 + 1):
            if 4 * i + 7 * j == N:
                return 'Yes'

    return 'No'

print(solve(11) == 'Yes')
print(solve(40) == 'Yes')
print(solve(3) == 'No')
