def solve(S):
    li = list(S)
    l  = len(li)
    sz = l - 2
    new_str = ''.join([li[0], str(sz), li[l-1]])

    return new_str

print(solve('internationalization') == 'i18n')
print(solve('smiles') == 's4s')
print(solve('xyz') == 'x1z')
