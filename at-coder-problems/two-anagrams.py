def solve(s, t):
    sl = list(s)
    tl = list(t)
    
    for i in sl:
        for j in tl:
            if i < j:
                return 'Yes'

    return 'No'

print(solve('yx', 'axy') == 'Yes')
print(solve('ratcode', 'atlas') == 'Yes')
print(solve('cd', 'abc') == 'No')
print(solve('zzz', 'zzz') == 'No')
