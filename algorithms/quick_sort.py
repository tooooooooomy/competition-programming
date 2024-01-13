def quick_sort(arr, l, r):
    if l >= r:
        return

    p = partition(arr, l, r)

    quick_sort(arr, l, p-1)
    quick_sort(arr ,p+1, r)

def partition(arr, l, r):
    pivot = arr[r]
    i = l-1

    for j in range(i+1, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1

arr = [2,1,4,3,14,-1, 5]
quick_sort(arr, 0, len(arr)-1)
print(arr)
