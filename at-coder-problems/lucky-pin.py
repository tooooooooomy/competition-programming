def solve(n, s):
    ans = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                s_c = s
                s_i = s_c.find(str(i))
                s_c = s_c[s_i+1:]
                s_j = s_c.find(str(j))
                s_c = s_c[s_j+1:]
                s_k = s_c.find(str(k))

                if s_i != -1 and s_j != -1 and s_k != -1:
                    ans += 1
    return ans


n = int(input())
s = input()
print(solve(n, s))

print(solve(4, '0224') == 3)
# print(solve(6, '123123') == 17)
# print(solve(19, '3141592653589793238') == 329)
# print(solve(19, '3141592653589793238'))
