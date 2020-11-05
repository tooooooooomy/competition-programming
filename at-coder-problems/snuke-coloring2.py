def solve(W, H, N, L):
    left, right, top, bottom = 0, W, H, 0
    for l in L:
        x, y, a = l[0], l[1], l[2]
        if a == 1:
            left = x
        elif a == 2:
            right = x
        elif a == 3:
            bottom = y
        else:
            top = y

    if right < left or top < bottom:
        return 0

    return (right - left) * (top - bottom)


print(solve(5, 4, 2, [[2, 1, 1], [3, 3, 4]]) == 9)
print(solve(5, 4, 3, [[2, 1, 1], [3, 3, 4], [1, 4, 2]]) == 0)
print(solve(10, 10, 5, [[1, 6, 1], [4, 1, 3], [6, 9, 4], [9, 4, 2], [3, 1, 3]]) == 64)
