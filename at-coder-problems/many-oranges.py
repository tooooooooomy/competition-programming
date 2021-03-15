A, B, W = map(int, input().split())

import math, sys

W *= 1000
m = math.ceil(W/B)
M = math.floor(W/A)

ans_m = sys.maxsize
ans_M = 0

a = A
b = B
a_n = 0
b_n = m
while b_n > 0:
  if b_n * b + a_n * a <= W:
      break
  if b_n * b + a_n * a > W:
    b_n -= 1
    a_n += 1

if  b_n * b + a_n * a > W:
  print('UNSATISFIABLE')
else:
  print((' ').join(str(x) for x in [m, M]))
