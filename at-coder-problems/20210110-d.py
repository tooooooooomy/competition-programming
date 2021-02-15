import sys

n, C = map(int, input().split())

event = []
for i in range(n):
    a, b, c = map(int, input().split())
    a -= 1
    event.append((a, c))
    event.append((b, -c))

event.sort()
ans = 0
fee = 0
p_day = 0

for day, cost in event:
    if day != p_day:
        ans += min(C, fee) * (day - p_day)
        p_day = day
    fee += cost

print(ans)
