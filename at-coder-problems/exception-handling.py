n = int(input())
A = [int(input()) for _ in range(n)]
sorted = sorted(A, reverse=True)
 
for i in range(n):
  c = A[i]
  if c == sorted[0]:
    print(sorted[1])
  else:
    print(sorted[0])
