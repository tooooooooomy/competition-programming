def solve(n, m, a):
    s_n = []
    for i in range(n):
        s = []
        j = 0
        while j < m-1:
            k = j + 1
            while k < m:
                s.append(max(a[i][j], a[i][k]))
                k += 1
            j += 1
        s_n.append(s)

    s_2 = [0] * len(s_n[0])
    for s in s_n:
        for i in range(len(s_n[0])):
            s_2[i] += s[i]

    return max(s_2)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
print(solve(n, m, a))

print(solve(1, 2, [[80, 84]]) == 84)
print(solve(3, 4, [[37, 29, 70, 41], [85, 69, 76, 50], [53, 10, 95, 100]]) == 250)

