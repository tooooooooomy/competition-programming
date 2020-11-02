def solve(A, B):
    s = A
    a = 0
    while s <= B:
        if s / 10000 == s % 10 and s / 1000 % 10 == s / 10 % 10:
            a += 1
        s += 1

    return a

print(solve(11009, 11332) == 4)
print(solve(31415, 92653) == 612)
