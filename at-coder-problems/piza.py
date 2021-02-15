import sys

d = int(input())
n = int(input())
m = int(input())
s = [0] * (n+1)
for i in range(1, n):
    s[i] = int(input())

s.append(d)
s = sorted(s)

k = [int(input()) for _ in range(m)]


res = 0

for i in range(m):
    ans = sys.maxsize
    left = 0
    right = n + 1
    while left <= right < n + 2:
        mid = (left + right) // 2
        ans = min(ans, abs(k[i] - s[mid]))
        if k[i] > s[mid]:
            left = mid + 1
        elif left == right:
            break
        else:
            right = mid

    res += ans

print(res)
