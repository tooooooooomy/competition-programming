n, m = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

h = {}
for a in A:
  h[a] = 1
  
for b in B:
  if b in h:
    del h[b]
  else:
    h[b] = 1

k = sorted(h.keys())
print(' '.join([str(i) for i in k]))
