n = int(input())
a = list(map(int, input().split()))
ans = [0] * n

for i in range(n):
    ans[a[i] - 1] = str(i+1)

print(" ".join(ans))
