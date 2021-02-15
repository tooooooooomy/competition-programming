N = int(input())
A = list(map(int, input().split()))
 
ans = 0
while True:
    print(A)
    for i in range(N):
        if A[i] % 2 != 0:
            break

        A[i] //= 2
    else:
        ans += 1
        continue
    break

print(ans)
