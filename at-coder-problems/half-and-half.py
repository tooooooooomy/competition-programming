def solve(A, B, C, X, Y):
    p_1 = max(X, Y) * C * 2

    p_2 = min(X, Y) * C * 2
    if X > Y:
        p_2 += A * (X-Y)
    else:
        p_2 += B * (Y-X)
    
    p_3 = A * X + B * Y

    return min(p_1, p_2, p_3)

a,b,c,x,y = map(int, input().split())
print(solve(a,b,c,x,y))

print(solve(1500, 2000, 1600, 3, 2) == 7900)
print(solve(1500, 2000, 1900, 3, 2) == 8500)
print(solve(1500, 2000, 500, 90000, 100000) == 100000000)
