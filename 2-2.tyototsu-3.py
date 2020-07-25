N = 6
A = 'ACDBCB'

def solve(N, A):
    t = ''
    a, b = 0, N - 1

    while a <= b:
        left = False
        for i in range(N):
            if A[a + i] < A[b - i]:
                left = True
                break
            elif A[a + i] > A[b - i]:
                left = False
                break
        if left:
            t += A[a]
            a += 1
        else:
            t += A[b]
            b -= 1

    return t



print(solve(N, A))
