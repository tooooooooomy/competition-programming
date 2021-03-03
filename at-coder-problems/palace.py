def solve(N, T, A, H):
    a = 0
    prev_d = 9999
    for i in range(N):
        av = T * H[i] * 0.006
        if abs(A - av) < prev_d:
            a = i + 1
            prev_d = abs(A - av)

    return a

print(solve(2, 12, 5, [1000, 2000]) == 1)
print(solve(3, 21, -11, [81234, 94124, 52141]) == 3)

n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
import sys
diff = sys.maxsize
ans = 0
for i in range(n):
  c_d = abs(1000 * a - (1000 * t - h[i] * 6))
  print(c_d)
  if c_d < diff:
    diff = c_d
    ans = i + 1
    
print(ans)
