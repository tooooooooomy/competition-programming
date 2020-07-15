import sys

def solve(N, M, matrix, s, g):
    dcol, drow = [1, 0, -1, 0], [0, 1, 0, -1]
    scol, srow = s[0], s[1]
    gcol, grow = g[0], g[1]

    d = []
    for row in range(M):
        d.append([])
        for col in range(N):
            d[row].append(sys.maxsize)

    queue = []
    queue.append(s)
    d[srow][scol] = 0

    while queue:
        current = queue.pop(0)
        ccol, crow = current[0], current[1]
        if ccol == gcol and crow == grow:
            break
        for i in range(3):
            ncol, nrow = ccol + dcol[i], crow + drow[i]

            if ncol > 0 and ncol < N and nrow > 0 and nrow < M and matrix[nrow][ncol] != '#' and d[nrow][ncol] == sys.maxsize:
                queue.append([ncol, nrow])
                d[nrow][ncol] = d[crow][ccol] + 1
    
    return d[grow][gcol]

N = 8
M = 10
s = [0, 1]
g = [6, 9]
matrix = [
        ['#', 'S', '#', '#', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '#'],
        ['.', '#', '.', '.', '.', '.', '.', '#'],
        ['.', '#', '.', '.', '.', '.', '.', '.'],
        ['#', '#', '.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '#', '#', '#', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '#'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '#', '.', '.', 'G', '.'],
]

print(solve(N, M, matrix, s, g))
