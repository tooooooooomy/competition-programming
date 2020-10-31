def solve(S):
    r = 700
    if S[0] == 'o':
        r += 100
    if S[1] == 'o':
        r += 100
    if S[2] == 'o':
        r += 100

    return r

print(solve('oxo') == 900)
print(solve('ooo') == 1000)
print(solve('xxx') == 700)
