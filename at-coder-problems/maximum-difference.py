def solve(N, A):
    a = 0
    for i in range(N-1):
        for j in range(1, N):
            tmp = abs(A[i] - A[j])
            if  tmp > a:
                a = tmp

    return a

print(solve(4, [1, 4, 6, 3]) == 5)
print(solve(2, [1000000000, 1]) == 999999999)
print(solve(5, [1, 1, 1, 1, 1]) == 0)
