def solve(N, A):
    l = []
    i = 0
    while i < N-1:
        a = []
        a.append(A[i])

        while i < N-1 and A[i] < A[i+1]:
            a.append(A[i+1])
            i += 1
        if len(a) > 1:
            l.append(a)
            a = []

        while i < N-1 and A[i] >= A[i+1]:
            a.append(A[i+1])
            i += 1
        if a:
            l.append(a)
            a = []

        i += 1

    print(l)
    return len(l)

print(solve(6, [1, 2, 3, 2, 2, 1]) == 2)
print(solve(9, [1, 2, 1, 2, 1, 2, 1, 2, 1]) == 5)
print(solve(7, [1, 2, 3, 2, 1, 9999, 10000]) == 3)
