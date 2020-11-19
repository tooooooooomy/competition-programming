def solve(n):
    ans = 0
    for i in range(105, n+1):
        if i % 2 == 0:
            continue

        a = 0
        for j in range(1, i+1):
            if i % j == 0:
                a += 1

        if a == 8:
            ans += 1

    return ans

n = int(input())
print(solve(n))

print(solve(105) == 1)
print(solve(7) == 0)
