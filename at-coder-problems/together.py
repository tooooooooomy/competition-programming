def solve(N, a):
    d = {}
    min_x = min(a) - 1
    max_x = max(a) + 1
    while min_x <= max_x:
        d[min_x] = 0
        min_x += 1

    for i in range(N):
        d[a[i] - 1] += 1
        d[a[i]] += 1
        d[a[i] + 1] += 1

    return max(d.values())

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))


print(solve(7, [3, 1, 4, 1, 5, 9, 2]) == 4)
print(solve(10, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3)
print(solve(1, [99999]) == 1)
