h, w, c = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
ans = float('inf')
dic = [[float('inf') for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i:
            dic[i][j] = min(dic[i][j], dic[i-1][j])
        if j:
            dic[i][j] = min(dic[i][j], dic[i][j-1])
        ans = min(ans, a[i][j]+(i+j)*c + dic[i][j])
        dic[i][j] = min(dic[i][j], a[i][j]-(i+j)*c)

a = a[::-1]
dic = [[float('inf') for _ in range(w)] for _ in range(h)]
for i in range(h):
    for j in range(w):
        if i:
            dic[i][j] = min(dic[i][j], dic[i-1][j])
        if j:
            dic[i][j] = min(dic[i][j], dic[i][j-1])
        ans = min(ans, a[i][j]+(i+j)*c + dic[i][j])
        dic[i][j] = min(dic[i][j], a[i][j]-(i+j)*c)

print(ans)
