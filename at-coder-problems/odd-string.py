def solve(s):
    sl = list(s)
    nl = []
    for i in range(len(sl)):
        if i % 2 == 0:
            nl.append(sl[i])

    return ''.join(nl)

print(solve('atcoder') == 'acdr')
print(solve('aaaa') == 'aa')
print(solve('z') == 'z')
print(solve('fukuokayamaguchi') == 'fkoaaauh')
