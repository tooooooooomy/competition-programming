def sieve(n):
    is_prime = [True] * (n+1)
    prime = []
    p = 0
    for i in range(2, n+1):
        if is_prime[i]:
            prime.append(i)
            p += 1
            for j in range(i * 2, n+1, i):
                is_prime[j] = False

    return p

print(sieve(11))
print(sieve(1000000))

def segment_sieve(a, b):
    is_prime_small = []
    is_prime = []
    i = 0
    while i * i < b:
        is_prime_small.append(True)
        i += 1

    i = 0
    for i in range(0, b-a):
        is_prime.append(True)

    i = 2
    while i * i < b:
        if is_prime_small[i]:
            j = 2 * i
            while j * j < b:
                is_prime_small[j] = False
                j += i

            j = max(2, (a + i - 1)) * i
            while j < b:
                is_prime[j-a] = False
                j += i

