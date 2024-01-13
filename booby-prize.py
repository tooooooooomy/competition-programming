n = int(input())
a = list(map(int, input().split()))

if a[1] > a[0]:
    last, booby = 1, 0
else:
    last, booby = 0, 1

for i in range(2, n):
  if a[i] > a[last]:
    booby = last
    last = i
  elif a[i] < a[last] and a[i] > a[booby]:
    booby = i

print(booby+1)
