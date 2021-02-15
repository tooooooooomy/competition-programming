n, a, b = map(int, input().split())
s = input()

cnt = 0
cnt_b = 0
a_b = a + b
s_l = len(s)

for i in range(s_l):
    if s[i] == 'c':
        print('No')
    elif s[i] == 'a':
        if cnt+1 <= a_b:
            print('Yes')
            cnt += 1
        else:
            print('No')

    else:
        if cnt+1 <= a_b and cnt_b+1 <= b:
            print('Yes')
            cnt += 1
        else:
            print('No')

        cnt_b += 1
