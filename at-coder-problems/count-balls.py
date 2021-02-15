N, A, B = map(int, input().split())

ans = N // (A+B) * A

a = N % (A+B)

print(ans + min(A, a))
