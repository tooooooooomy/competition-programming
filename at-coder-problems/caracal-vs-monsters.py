H = int(input())

ans = 1
a = 1
while H > 1:
    H //= 2
    ans += 2 ** a
    a += 1

print(ans)
