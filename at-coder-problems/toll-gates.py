n, m, x = map(int, input().split())
a = list(map(int, input().split()))

a.append(x)
a.sort()

def binary_search(l, r, x):
    m = (r+l) // 2
    if a[m] == x:
        return m
    elif a[m] > x:
        return binary_search(l, m, x)
    else:
        return binary_search(m+1, r, x)

i = binary_search(0, m, x)

print(min(i, m-i))
