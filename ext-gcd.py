def extGCD(a, b):
    if b == 0:
        x = 1
        y = 0
        d = a
    else:
        d, y, x = extGCD(b, a % b)
        y -= a / b * x

    return d, x, y

print(extGCD(111, 30))

