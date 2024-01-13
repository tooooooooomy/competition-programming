def qs(arr, l, r):
    if l >= r:
        return

    p = pertition(arr, l, r)

    qs(arr, l, p-1)
    qs(arr, p+1, r)


def pertition(arr, l, r):
    pivot = arr[r]
    i = l-1

    for j in range(l, r):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[r] = arr[r], arr[i+1]

    return i+1

a = [1,6,5,2,3]
qs(a, 0, len(a)-1)
print(a)
