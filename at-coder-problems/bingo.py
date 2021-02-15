a = []

for i in range(3):
    a.append(list(map(int, input().split())))

n = int(input())

b = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(3):
        for k in range(3):
            if b[i] == a[j][k]:
                a[j][k] = -1


if a[0][0] == a[0][1] == a[0][2] == -1 or \
   a[1][0] == a[1][1] == a[1][2] == -1 or \
   a[2][0] == a[2][1] == a[2][2] == -1 or \
   a[0][0] == a[1][0] == a[2][0] == -1 or \
   a[0][1] == a[1][1] == a[2][1] == -1 or \
   a[0][2] == a[1][2] == a[2][2] == -1 or \
   a[0][0] == a[1][1] == a[2][2] == -1 or \
   a[2][0] == a[1][1] == a[0][2] == -1:
    print('Yes')
else:
    print('No')
