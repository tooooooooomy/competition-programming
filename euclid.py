P1 = [1, 11]
P2 = [5, 3]

def solve(p1, p2):
    x = abs(p2[0] - p1[0])
    y = abs(p2[1] - p1[1])

    print(gcd(x, y) - 1)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

solve(P1, P2)
