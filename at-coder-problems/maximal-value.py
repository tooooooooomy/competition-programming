n = int(input())
B = list(map(int, input().split()))

ans = B[n-2]
i = n-2

while i > 0:
    ans += min(B[i], B[i-1])
    i -= 1

ans += B[0]
print(ans)
