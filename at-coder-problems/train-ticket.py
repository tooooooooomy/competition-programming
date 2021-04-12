s = input()

a, b, c, d = int(s[0]), int(s[1]), int(s[2]), int(s[3])

pat = [
  ['+', '+', '+'],
  ['+', '+', '-'],
  ['+', '-', '+'],
  ['-', '+', '+'],
  ['-', '-', '+'],
  ['-', '+', '-'],
  ['+', '-', '-'],
  ['-', '-', '-'],
]
for op1, op2, op3 in pat:
  su = a
  f1, f2, f3 = False, False, False
  if op1 == '+':
    su += b
    f1 = True
  else:
    su -= b
  if op2 == '+':
    f2 = True
    su += c
  else:
    su -= c
  if op3 == '+':
    f3 = True
    su += d
  else:
    su -= d
    
  if su == 7:
    s = []
    s.append(str(a))
    if f1:
      s.append('+')
    else:
      s.append('-')
    s.append(str(b))
    if f2:
      s.append('+')
    else:
      s.append('-')
    s.append(str(c))
    if f3:
      s.append('+')
    else:
      s.append('-')
    s.append(str(d))
    s.append('=')
    s.append('7')
    
    print(''.join(s))
    exit()
