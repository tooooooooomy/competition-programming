def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j] > arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

arr = [2,1,4,3,14,-1, 5]
insertion_sort(arr)
print(arr)
