c1, c5, c10, c50, c100, c500, A = 3, 2, 1, 3, 0, 2, 620
C = [3, 2, 1, 3, 0, 2]
A = 620

def donyoku2(C, A):
    v = [1, 5, 10, 50, 100, 500]
    ans = 0

    for i in reversed(range(6)):
        print(i)
        t = min(A // v[i], C[i])
        A -= v[i] * t
        ans += t

    return ans

print(donyoku2(C, A))

def donyoku(c1, c5, c10, c50, c100, c500, A):
    res = 0
    while A > 0:
        if A >= 500 and c500 > 0:
            res += 1
            c500 -= 1
            A -= 500
        elif A >= 100 and c100 > 0:
            res += 1
            c100 -= 1
            A -= 100
        elif A >= 50 and c50 > 0:
            res += 1
            c50 -= 1
            A -= 50
        elif A >= 10 and c10 > 0:
            res += 1
            c10 -= 1
            A -= 10
        elif A >= 5 and c5 >0:
            res += 1
            c5 -= 1
            A -= 5
        elif A >= 1 and c1 > 0:
            res += 1
            c1 -= 1
            A -= 1
        else:
            return 0

    return res

print(donyoku(c1, c5, c10, c50, c100, c500, A))
