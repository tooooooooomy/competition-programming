import itertools

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]

combi = []
ans = 0
for balls in (itertools.product(*cd)):
        balls = set(balls)
        cnt = 0
        for a, b in ab:
            if a in balls and b in balls:
                cnt += 1

            ans = max(ans, cnt)

print(ans)
