def solve(n, a):
    ans1 = 0
    sum_n = 0

    for i in range(n):
        if i % 2 == 0:
            if sum_n + a[i] <= 0:
                ans1 += abs(sum_n + a[i]) + 1
                sum_n = 1
            else:
                sum_n += a[i]
        else:
            if sum_n + a[i] >= 0:
                ans1 += abs(sum_n + a[i]) + 1
                sum_n = -1
            else:
                sum_n += a[i]

    ans2 = 0
    sum_n = 0
    for i in range(n):
        if i % 2 == 0:
            if sum_n + a[i] >= 0:
                ans2 += abs(sum_n + a[i]) + 1
                sum_n = -1
            else:
                sum_n += a[i]
        else:
            if sum_n + a[i] <= 0:
                ans2 += abs(sum_n + a[i]) + 1
                sum_n = 1
            else:
                sum_n += a[i]

    return min(ans1, ans2)

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))


print(solve(4, [1, -3, 1, 0]) == 4)
print(solve(5, [3, -6, 4, -5, 7]) == 0)
print(solve(6, [-1, 4, 3, 2, -5, 4]) == 8)
