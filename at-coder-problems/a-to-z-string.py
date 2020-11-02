def solve(s):
    st = 0
    ed = 0
    for i in range(len(s)):
        if s[i] == 'A' and st == 0:
            st = i
        if s[i] == 'Z':
            ed = i

    return ed - st + 1


print(solve('QWERTYASDFZXCV') == 5)
print(solve('ZABCZ') == 4)
print(solve('HASFJGHOGAKZZFEGA') == 12)
