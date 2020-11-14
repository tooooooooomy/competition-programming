def solve(n, a):
    odd_c = 0
    for i in range(n):
        if a[i] % 2 == 1: odd_c += 1

    return 'YES' if odd_c % 2 == 0 else 'NO'

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))


print(solve(1, [1]) == 'YES')
print(solve(3, [1, 2, 3]) == 'YES')
print(solve(5, [1, 2, 3, 4, 5]) == 'NO')
print(solve(6, [1, 2, 3, 4, 5, 6]) == 'NO')
