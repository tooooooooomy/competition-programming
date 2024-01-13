def ms(arr):
    merge_sort(0, len(arr)-1, arr)

def merge_sort(l, r, arr):
    print(l, r)
    if l >= r:
        return

    m = (l+r)//2

    merge_sort(l, m, arr)
    merge_sort(m+1, r, arr)

    left = arr[l:m+1]
    right = arr[m+1:r+1]

    original = l
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[original] = right[j]
            j += 1
        else:
            arr[original] = left[i]
            i += 1
        original += 1

    while i < len(left):
        arr[original] = left[i]
        original += 1
        i += 1
    while j < len(right):
        arr[original] = right[j]
        original += 1
        j += 1


arr = [4, 3, 2, 5, 8, 7]

ms(arr)

print(arr)
