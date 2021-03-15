s = input()
k = int(input())

l = len(s)
for i in range(l):
    if i < k and s[i] != '1':
        print(s[i])
        exit()

print(1)
