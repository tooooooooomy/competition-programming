def solve(s):
    ans = 0
    tmp = 0
    for i in s:
        if i in ['A', 'C', 'G', 'T']:
            tmp += 1
        else:
            tmp = 0

        ans = max(ans, tmp)

    return ans

# s = input()
# print(solve(s))

print(solve('ATCODER') == 3)
print(solve('HATAGAYA') == 5)
print(solve('SHINJUKU') == 0)
print(solve('A') == 1)
print(solve('ATCRHATAGA') == 10)
