import sys
sys.setrecursionlimit(300000)
from sys import stdin
from collections import defaultdict
import math
import heapq
import copy
# from sortedcontainers import sortedset

def main():
    n = int(input())
    t = list(map(int, input().split()))

    dic = defaultdict(bool)

    for i in range(n):
        zeros = t[i]


main()
