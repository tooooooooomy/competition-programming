s = input()
 
if s[0] != 'A':
  print('WA')
  exit()
 
if s[1].isupper() or s[-1].isupper():
  print('WA')
  exit()

c = False
for i in range(2, len(s)-1):
  if s[i] == 'C':
    if c:
      print('WA')
      exit()
    else:
      c = True
  elif s[i].isupper():
    print('WA')
    exit()

if c:
  print('AC')
else:
  print('WA')

