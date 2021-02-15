alphabets = list('abcdefghijklmnopqrstuvwxyz')
S = input()
 
for c in S:
  if c in alphabets:
    alphabets.remove(c)
  
  if not alphabets:
    print('None')
    exit()
    
print(alphabets[0])
