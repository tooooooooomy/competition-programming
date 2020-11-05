def solve(N, M, s, t):
    dic = {}
    for i in range(N):
        if not s[i] in dic:
            dic[s[i]] = 0

        dic[s[i]] += 1

    for i in range(M):
        if not t[i] in dic:
            dic[t[i]] = 0

        dic[t[i]] -= 1

    a = 0
    for k in dic:
        if dic[k] > a:
            a = dic[k]

    return a

print(solve(3, 1, ['apple', 'apple', 'orange'], ['grape']) == 2)
print(solve(3, 5, ['apple', 'apple', 'orange'], ['apple', 'apple', 'apple', 'apple', 'apple']) == 1)
print(solve(1, 10, ['voldemort'], ['voldemort', 'voldemort', 'voldemort', 'voldemort', 'voldemort', 'voldemort', 'voldemort', 'voldemort', 'voldemort', 'voldemort']) == 0)
print(solve(6, 5, ['red', 'red', 'blue', 'yellow', 'yellow', 'red'], ['red', 'red', 'yellow', 'green', 'blue']) == 1)
