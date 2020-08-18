N = 3
L = [8, 5, 8]

ans = 0

import Queue as Q
que = Q.PriorityQueue()
for i in range(N):
    que.put(L[i])

while que.qsize() > 1:
    l1 = que.get()
    l2 = que.get()

    ans += l1 + l2

    que.put(l1 + l2)

print(ans)
