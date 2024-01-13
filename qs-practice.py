def qs(array):
    quicksort(0, len(array)-1, array)

def quicksort(l, r, array):
    if l >= r:
        return

    partition = array[r]

    j = l-1

    for i in range(l, r):
        if array[i] < partition:
            j += 1
            array[i], array[j] = array[j], array[i]

    j += 1
    array[r], array[j] = array[j], array[r]

    quicksort(l, j-1, array)
    quicksort(j+1, r, array)



arr = [1, 8, 7, 5, 4, 6]

qs(arr)

print(arr)
