h,w,x,y = map(int, input().split())

s = [list(input()) for _ in range(h)]

ans = 1

row, col = x-2, y-1

while row >= 0:
    if s[row][col] == '#':
        break
    else:
        ans += 1
        row -= 1

row = x
while row < h:
    if s[row][col] == '#':
        break
    else:
        ans += 1
        row += 1

row = x-1
col = y-2
while col >= 0:
    if s[row][col] == '#':
        break
    else:
        ans += 1
        col -= 1

col = y
while col < w:
    if s[row][col] == '#':
        break
    else:
        ans += 1
        col += 1

print(ans)
