arr = [int(input()) for _ in range(5)]

la = 10
lai = 99999999999

for i in range(5):
  c = arr[i] % 10

  if c != 0 and la > c:
      la = c
      lai = i

if lai == 99999999999:
    lai = 0

arr[lai], arr[4] = arr[4], arr[lai]

ans = 0
for i in range(4):

    ans += arr[i]

    if arr[i] % 10 != 0:
        ans += 10 - arr[i] % 10

print(ans + arr[4])
