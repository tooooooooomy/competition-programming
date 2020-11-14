def solve(n, a):
    dic = {}

    for i in a:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    ans = 0
    for k in dic:
        if dic[k] % 2 == 1:
            ans += 1

    return ans

n = int(input())
a = [int(input()) for _ in range(n)]
print(solve(n, a))

print(solve(3, [6, 2, 6]) == 1)
print(solve(4, [2, 5, 5, 2]) == 0)
print(solve(6, [12, 22 ,16, 22, 18, 12]) == 2)
