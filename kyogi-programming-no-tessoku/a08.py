# 5 5
# 2 0 0 5 1
# 1 0 3 0 0
# 0 8 5 0 2
# 4 1 0 0 6
# 0 9 2 7 0
# 2
# 2 2 4 5
# 1 1 5 5
H, W = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(H)]
Q = int(input())
A, B, C, D = [0] * Q, [0] * Q, [0] * Q, [0] * Q

for i in range(Q):
    a, b, c, d = map(int, input().split())
    A[i], B[i], C[i], D[i] = a, b, c, d

X = [[0] * W for _ in range(H)]

for row in range(H):
    for col in range(W):
        X[row][col] += mat[row][col]
        if col > 0:
            X[row][col] += X[row][col-1]

for row in range(1, H):
    for col in range(W):
        X[row][col] += X[row-1][col]

ans = [0] * Q
for i in range(Q):
    ans[i] = X[C[i]-1][D[i]-1]
    if A[i] > 1 and B[i] > 1:
        ans[i] += X[A[i]-2][B[i]-2]
    if B[i] > 1:
        ans[i] -= X[C[i]-1][B[i]-2]
    if A[i] > 1:
        ans[i] -= X[A[i]-2][D[i]-1]

print(ans)
