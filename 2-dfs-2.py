from typing import List, Dict

def solve(N, M, matrix):
    res = 0
    for row in range(M):
        for col in range(N):
            if matrix[row][col] == 'W':
                print('hoge')
                dfs(N, M, matrix, col, row)
                res += 1

    return res

def dfs(N: int, M: int, matrix: List[int], col: int, row: int):
    print('fuga')
    matrix[row][col] = '.'

    dcol = -1
    drow = -1

    while dcol <= 1:
        drow = -1
        while drow <= 1:
            ncol, nrow = dcol + col, drow + row

            if (ncol >= 0 and ncol < N) and (nrow >= 0 and nrow < M) and matrix[nrow][ncol] == 'W':
                dfs(N, M, matrix, ncol, nrow)

            drow += 1

        dcol += 1

N = 10
M = 12
matrix = [
        ['.', 'W', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', 'W', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['W', '.', 'W', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'W', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'W', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'W', 'W', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', 'W', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', 'W', '.', '.', '.', '.', '.', '.']
]

print(solve(N, M, matrix))
