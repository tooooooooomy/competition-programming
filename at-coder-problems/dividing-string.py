s = input()
n = len(s)

prev = ''
ans = 0
i = 0
while i < n:
    c = s[i]

    if c == prev:
        i += 1
        if i == n:
            break

        c += s[i]

    prev = c
    i += 1
    ans += 1

print(ans)

s = input()

dp = [[0] * 2 for _ in range(len(s))]

dp[0][0] = 1
dp[0][1] = 0
dp[1][0] = 2 if s[0] != s[1] else 0
dp[1][1] = 1

for i in range(2, len(s)):
  if s[i] != s[i-1]:
    dp[i][0] = max(dp[i-1]) + 1
  else:
    dp[i][0] = dp[i-1][1] + 1
  
  dp[i][1] = max(dp[i-2]) + 1
  
print(max(dp[-1]))
