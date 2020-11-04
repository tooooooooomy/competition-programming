def solve(s):
    sorted_s = sorted(s)
    l_s = len(s)
    alphabets = list('abcdefghijklmnopqrstuvwxyz')
    j = 0
    for i in range(len(alphabets)):
        if alphabets[i] != sorted_s[j]:
            return alphabets[i]
        
        while j < l_s and alphabets[i] == sorted_s[j]:
            j += 1

    return 'None'

print(solve('atcoderregularcontest') == 'b')
print(solve('abcdefghijklmnopqrstuvwxyz') == 'None')
print(solve('fajsonlslfepbjtsaayxbymeskptcumtwrmkkinjxnnucagfrg') == 'd')
