def solve(N):
    if N == 1:
        return 1

    a = 2
    while a <= N:
        a *= 2

    if a > N:
        a //= 2

    return a

N = int(input())
print(solve(N))

print(solve(7) == 4)
print(solve(32) == 32)
print(solve(1) == 1)
print(solve(100) == 64)
