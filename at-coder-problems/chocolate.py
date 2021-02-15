N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
 
ans = 0
for i in range(N):
  d = 1
  c = 1
  while d <= D:
    ans += 1

    d = A[i] * c + 1
    c += 1

ans += X
print(ans)
