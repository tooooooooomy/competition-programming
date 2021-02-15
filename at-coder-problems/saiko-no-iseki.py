import itertools

def solve(n, a):
    ans = 0

    for p1, p2 in itertools.combinations(a, 2):
        x = p2[0] - p1[0]
        y = p2[1] - p1[1]

        if (p1[0] - y, p1[1] + x) in a and (p2[0] - y, p2[1] + x) in a:
            ans = max(ans, x ** 2 + y ** 2)

    return ans

n = int(input())
a = set()
for i in range(n):
    x, y = map(int, input().split())
    a.add((x, y))

print(solve(n, a))
