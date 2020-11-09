import sys

def solve(N, L):
    h = 0
    x_max = 0
    y_max = 0
    for l in L:
        h = min(h, l[2])
        x_max = max(x_max, l[0])
        y_max = max(y_max, l[1])

    n_max = sys.maxsize
    while h < n_max:
        c_x = 0
        while c_x <= x_max:
            c_y = 0
            while c_y <= y_max:
                a = True
                for l in L:
                    if h - abs(l[0] - c_x)  - abs(l[1] - c_y) != l[2]:
                        a = False

                if a == True:
                    return [c_x, c_y, h]

                c_y += 1
            c_x += 1
        h += 1

    return [0, 0, 0]



print(solve(4, [[2, 3, 5], [2, 1, 5], [1, 2, 5], [3, 2, 5]]) == [2, 2, 6])
print(solve(2, [[0, 0, 100], [1, 1, 98]]) == [0, 0, 100])
print(solve(3, [[99, 1, 191], [100, 1, 192], [99, 0, 192]]) == [100, 0, 193])
