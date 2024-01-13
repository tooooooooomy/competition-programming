x, y, z = map(int, input().split())

import math
a = math.floor(y*z/x)

while y / x <= a / z:
    a -= 1

print(a)
