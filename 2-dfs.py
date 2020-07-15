from typing import List

n = 4
a = [1, 2, 4, 7]
k=13

def dfs(n: int, a: List[int], k: int):
    sum = 0
    i = 0
    return dfs_helper(n, a, k, sum, i)


def dfs_helper(n: int, a: List[int], k: int, sum: int, i: int) -> bool:
    if sum == k:
        return True

    if n == i:
        return False

    if dfs_helper(n, a, k, sum + a[i], i + 1):
        return True

    if dfs_helper(n, a, k, sum, i + 1):
        return True

print(dfs(n, a, k))
