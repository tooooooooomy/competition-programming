n = int(input())
k = int(input())
x = list(map(int, input().split()))

ans = 0
for i in range(n):
    a = (x[i]) * 2
    b = (k-x[i]) * 2
    ans += min(a, b)

print(ans)
