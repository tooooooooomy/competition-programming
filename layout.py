N = 4
ML = 2
MD = 1
AL = [1, 2]
BL = [3, 4]
DL = [10, 20]
AD = [2]
BD = [3]
DD = [3]

d = [9999] * N
d[0] = 0

def solve():
    for k in range(N):
        for i in range(N-1):
            if d[i + 1] < 9999:
                d[i] = min(d[i], d[i + 1])
        # From AL To BL, cost DL
        for i in range(ML):
            if d[AL[i] - 1] < 9999:
                d[BL[i] - 1] = min(d[BL[i] - 1], d[AL[i] - 1] + DL[i])

        # From BD To AD, cost DD
        for i in range(MD):
            if d[BD[i] - 1] < 9999:
                d[AD[i] - 1] = min(d[AD[i] - 1], d[BD[i] - 1] - DD[i])

    res = d[N-1]
    if d[0] < 0:
        res = -1
    elif res == 9999:
        res = -2

    print(res)

solve()
