import Queue as Q

N = 4
L = 25
P = 10
A = [10, 14, 20, 21]
B = [10, 5, 2, 4]

A.append(L)
B.append(0)
N += 1

que = Q.PriorityQueue()

ans = 0
pos = 0
tank = P

for i in range(N):
    d = A[i] - pos
    
    while tank - d < 0:
        if que.empty():
            print(-1)
            exit()
        
        tank += que.get()[1]
        ans += 1

    tank -= d
    pos = A[i]
    que.put((-B[i], B[i]))
    
print(ans)

