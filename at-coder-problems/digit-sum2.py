n = int(input())

if n < 10:
  print(n)
  exit()
 
s = 0
k = 0
t = n
arr = []
while t > 0:
    k += 1
    arr.append(t % 10)
    t //= 10

arr.reverse()
s += (k-1) * 9 + (n // (10 ** (k-1))-1)

t = True
for a in arr[1:]:
    if a != 9:
        t = False
        break

if t:
    s += 1

print(s)

