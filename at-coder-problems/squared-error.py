n = int(input())
a = list(map(int, input().split()))

cnt = {}

for i in range(n):
    if a[i] in cnt:
        cnt[a[i]] += 1
    else:
        cnt[a[i]] = 1

sorted_key = sorted(cnt.keys())

s = 0
for i in range(1, len(sorted_key)):
    for j in range(i):
        s += cnt[sorted_key[i]] * cnt[sorted_key[j]] * (sorted_key[i] - sorted_key[j]) ** 2

print(s)
