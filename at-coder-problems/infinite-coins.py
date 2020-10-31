def solve(N, A):
    mod = N % 500

    if A >= mod:
        return 'YES'
    else:
        return 'NO'

print(solve(2018, 218) == 'YES')
print(solve(2763, 0) == 'NO')
print(solve(37, 514) == 'YES')
