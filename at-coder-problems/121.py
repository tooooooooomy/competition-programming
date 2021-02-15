a, b = map(str, input().split())

c = int(a + b)

ans = 1
while ans < c // 2:
    if ans ** 2 == c:
        print('Yes')
        exit()

    ans += 1

print('No')
