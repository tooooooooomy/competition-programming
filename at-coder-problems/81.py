def solve(N):
    for i in range(1, 10):
        for j in range(1, 10):
            if i * j == N:
                return 'Yes'

    return 'No'

print(solve(10) == 'Yes')
print(solve(50) == 'No')
print(solve(81) == 'Yes')
