H, W, N = map(int, input().split())
A, B, C, D = [0] * N, [0] * N, [0] * N, [0] * N
for i in range(N):
    A[i], B[i], C[i], D[i] = map(int, input().split())

mat = [[0] * (W+2) for _ in range(H+2)]
for i in range(N):
    mat[A[i]][B[i]] += 1
    mat[A[i]][D[i]+1] -= 1
    mat[C[i]+1][B[i]] -= 1
    mat[C[i]+1][D[i]+1] += 1

for row in range(1, H+1):
    for col in range(1, W+1):
        mat[row][col] += mat[row-1][col]
for row in range(1, H+1):
    for col in range(1, W+1):
        mat[row][col] += mat[row][col-1]

print(mat)

