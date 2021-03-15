S = list(input())

ans = 0
one = 0
zero = 0

for s in S:
    if s == '1':
        one += 1
    else:
        zero += 1

if one > 0 and zero > 0:
    ans = min(one, zero) * 2

print(ans)
