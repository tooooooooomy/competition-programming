N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

import itertools

a = list(itertools.permutations(P))
a.sort()
print(abs(a.index(P) - abs(a.index(Q))))
