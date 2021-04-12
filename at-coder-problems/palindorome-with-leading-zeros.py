s = input()

if s == '0':
    print('Yes')
    exit()

n = -1
c = 0
while s[n] == "0":
    c += 1
    n -= 1

for i in range((len(s)-c) // 2):
    if s[i] != s[n-i]:
        print("No")
        exit()
  
print("Yes")
