N = int(input())
while N % 2 == 0:
    N //= 2

sq = int(N ** 0.5)
ans = 0
for i in range(1, sq+1):
    if N % i == 0:
        ans += 2

if sq ** 2 == N:
    ans -= 1

print(ans * 2)
