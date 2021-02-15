n = int(input())
a = list(map(int, input().split()))

def win(arr, l, r):
    if r - l == 1:
        if arr[r] > arr[l]:
            return r
        else:
            return l
    else:
        m = (l + r) // 2

        l_win = win(arr, l, m)
        r_win = win(arr, m+1, r)

        if  arr[l_win] < arr[r_win]:
            return r_win
        else:
            return l_win

m = 2 ** n // 2

if n > 1:
    l_win = win(a, 0, m-1)
    r_win = win(a, m, len(a) - 1)
else:
    l_win = 0
    r_win = 1

if a[l_win] > a[r_win]:
    print(r_win+1)
else:
    print(l_win+1)
