def qs(arr, l, r):
    if l >= r:
        return

    p = partition(arr, l, r)

    qs(arr, l, p-1)
    qs(arr, p+1, r)


def partition(arr, l, r):
    pivot = arr[r]
    i = l-1

    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1

def ms(arr, l, r):
    if l >= r:
        return

    m = (l+r)//2
    ms(arr, l, m)
    ms(arr, m+1, r)

    left = arr[l:m+1]
    right = arr[m+1:r+1]

    i, j, k = 0, 0, l

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1

        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
      

arr = [3,5,1,-1,8,2]
qs(arr, 0, len(arr)-1)

print(arr)

arr = [3,5,1,-1,8,2]
ms(arr, 0, len(arr)-1)

print(arr)
