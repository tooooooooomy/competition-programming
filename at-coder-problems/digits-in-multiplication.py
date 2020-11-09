import sys

def solve(N):
    a = 1
    min_a = sys.maxsize

    while a ** 2 <= N:
        if N % a == 0:
            b = N / a
            min_a = min(min_a, max(digits(a), digits(b)))

        a += 1

    return min_a

def digits(n):
    a = 1
    while n / 10 > 0:
        a += 1
        n /= 10

    return a

print(solve(10000) == 3)
print(solve(1000003) == 7)
print(solve(9876543210) == 6)
