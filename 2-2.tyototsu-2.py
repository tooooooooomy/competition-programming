n = 5
s = [1, 2, 4, 6, 8]
t = [3, 5, 7, 9, 10]

def solve(n, s, t):
    ans = 0
    inv = []
    for i in range(len(s)):
        inv.append([t[i], s[i]])

    inv.sort
    threshold = 0
    for i in range(len(s)):
        if threshold < inv[i][1]:
            ans += 1
            threshold = inv[i][0]

    return ans

a = solve(n, s, t)
print(a)
