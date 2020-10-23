def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if i * i > n:
            break
        elif n % i == 0:
            return False

    return True

print(is_prime(295927))
print(is_prime(53))

def divisor(n):
    res = []
    for i in range(1, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            res.append(i)
            if i != n / i:
                res.append(n / i)

    return res


print(divisor(232455))

def prime_factor(n):
    res = {}
    for i in range(2, n+1):
        if i * i > n:
            break
        while n % i == 0:
            if not i in res:
                res[i] = 0

            res[i] += 1
            n /= i
    
    if n != 1:
        res[n] = 1

    return res

print(prime_factor(100))
