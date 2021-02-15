a, b, c = map(int, input().split())

if a % 2 != 0 or b % 2 != 0 or c % 2 != 0:
    print(0)
    exit()

if a == b == c:
    print(-1)
    exit()

ans = 0
while a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
    d_a = a // 2
    d_b = b // 2
    d_c = c // 2
    a = d_b + d_c
    b = d_a + d_c
    c = d_a + d_b
    ans += 1

print(ans)
