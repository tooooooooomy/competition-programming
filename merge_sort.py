def ms(arr, l, r):
    if l >= r:
        return

    m = (l+r)//2

    ms(arr, l, m)
    ms(arr, m+1, r)

    left = arr[l:m+1]
    right = arr[m+1:r+1]

    i, j = 0, 0
    orig = l

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[orig] = left[i]
            i += 1
        else:
            arr[orig] = right[j]
            j += 1

        orig += 1

    while i < len(left):
        arr[orig] = left[i]
        orig += 1
        i += 1

    while j < len(right):
        arr[orig] = right[j]
        orig += 1
        j += 1

arr = [2,1,4,3,14,-1, 5]
ms(arr, 0, len(arr)-1)
print(arr)
