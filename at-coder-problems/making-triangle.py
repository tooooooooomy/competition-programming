def solve(N, L):
    a = 0
    for i in range(N-2):
        for j in range(1, N-1):
            if i >= j:
                continue
            for k in range(2, N):
                if j >= k:
                    continue

                if L[i] == L[j] or L[i] == L[k] or L[j] == L[k]:
                    continue

                if not abs(L[i] - L[j]) < L[k] < L[i] + L[j]:
                    continue

                a += 1


    return a

print(solve(5, [4, 4, 9, 7, 5]) == 5)
print(solve(6, [4, 5, 4, 3, 3, 5]) == 8)
print(solve(10, [9, 4, 6, 1, 9, 6, 10, 6, 6, 8]) == 39)
print(solve(2, [1, 1]) == 0)
