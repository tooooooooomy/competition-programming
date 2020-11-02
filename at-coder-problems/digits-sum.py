import sys

def solve(N):
    mi = sys.maxsize
    a = 1

    while a <= N / 2:
        mi = min(mi, sum_of_digit(a) + sum_of_digit(N-a))
        a += 1

    return mi

def sum_of_digit(n):
    s = 0

    while n > 0:
        s += n % 10
        n /= 10

    return s

print(solve(15) == 6)
print(solve(100000) == 10)
