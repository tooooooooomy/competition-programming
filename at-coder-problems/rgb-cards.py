def solve(r, g, b):
    if (r * 100 + g * 10 + b) % 4 == 0:
        print("YES")
    else:
        print("NO")

solve(4, 3, 2)
solve(2, 3, 4)
