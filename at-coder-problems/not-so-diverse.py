def solve(N, K, A):
    dic = {}
    for a in A:
        if not a in dic:
            dic[a] = 0

        dic[a] += 1

    k = len(dic)
    if k <= K:
        return 0

    sorted_vals = sorted(dic.values())

    ans = 0
    i = 0
    while k < K:
        ans += sorted_values[i]
        i += 1
        k -= 1

    return ans


print(solve(5, 2, [1, 1, 2, 2, 5]) == 1)
print(solve(4, 4, [1, 1, 2, 2]) == 0)
print(solve(10, 3, [5, 1, 3, 2, 4, 1, 1, 2, 3, 4]) == 3)
