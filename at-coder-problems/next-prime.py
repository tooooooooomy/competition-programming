x = int(input())

def isPrime(x):
    h = x // 2
    i = 2
    while i <= h:
        if x % i == 0:
            return False

        i += 1

    return True

while True:
    if isPrime(x):
        print(x)
        break

    x += 1
