def solve(n, a, b):
    ans = ''
    if (b-a) % 2 == 1:
        ans = 'Borys'
    else:
        ans = 'Alice'

    return ans

n, a, b = map(int, input().split())
print(solve(n, a, b))


print(solve(5, 2, 4) == 'Alice')
print(solve(2, 1, 2) == 'Borys')
print(solve(58, 23, 42) == 'Borys')
