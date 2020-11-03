def solve(N, x, a):
    sorted_a = sorted(a)
    ans = 0
    for i in range(N):
        if x <= 0:
            break
        x -= sorted_a[i]
        
        if x >= 0:
            ans += 1

    if x > 0:
        ans -= 1

    return ans


print(solve(3, 70, [20, 30, 10]) == 2)
print(solve(3, 10, [20, 30, 10]) == 1)
print(solve(4, 1111, [1, 10, 100, 1000]) == 4)
print(solve(2, 10, [20, 20]) == 0)
