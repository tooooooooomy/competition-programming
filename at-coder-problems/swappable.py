n = int(input())
a = list(map(int, input().split()))

dic = {}
for i in range(n):
    if a[i] not in dic:
        dic[a[i]] = 1
    else:
        dic[a[i]] += 1

ans = n * (n-1) // 2
for k in dic:
    if dic[k] > 1:
        ans -= dic[k] * (dic[k]-1) // 2

print(ans)


