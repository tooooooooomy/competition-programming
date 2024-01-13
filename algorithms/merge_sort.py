def merge_sort(arr, l, r):
    if l >= r:
        return

    m = (l+r)//2
    merge_sort(arr, l, m)
    merge_sort(arr, m+1, r)
    
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    original = l

    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[original] = left[i]
            i += 1
        else:
            arr[original] = right[j]
            j += 1

        original += 1

    while i < len(left):
        arr[original] = left[i]
        original += 1
        i += 1
    while j < len(right):
        arr[original] = right[j]
        j += 1
        original += 1


arr = [2,1,4,3,14,-1, 5]
merge_sort(arr, 0, len(arr)-1)
print(arr)
