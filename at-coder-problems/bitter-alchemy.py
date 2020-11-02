def solve(N, X, M):
    rem = X - sum(M)
    mim = min(M)
    a = len(M)

    while rem - mim > 0:
        a += 1
        rem -= mim

    return a

print(solve(3, 1000, [120, 100, 140]) == 9)
print(solve(4, 360, [90, 90, 90, 90]) == 4)
print(solve(5, 3000, [150, 130, 150, 130, 110]) == 26)
