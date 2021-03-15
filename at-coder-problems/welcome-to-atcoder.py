n, m = map(int, input().split())

arr = []
for i in range(m):
  p, s = input().split()
  arr.append([p, s])

wa, ac = [0] * (n+1), [False] * (n+1)
acnum, wanum = 0, 0

for i in range(m):
    p, s = arr[i]
    p = int(p)

    if ac[p]:
        continue
    if s == 'AC':
        ac[p] = True
        acnum += 1
        wanum += wa[p]
    else:
        wa[p] += 1

print(acnum, wanum)
