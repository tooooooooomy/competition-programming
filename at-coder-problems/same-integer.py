def solve(a, b, c):
    sorted_array = sorted([a, b, c])

    ans = 0
    while not (sorted_array[0] == sorted_array[1] and sorted_array[1] == sorted_array[2] and sorted_array[0] == sorted_array[2]):
        max_v = sorted_array[2]
        mid_v = sorted_array[1]
        min_v = sorted_array[0]

        if mid_v == min_v:
            sorted_array[0] += 1
            sorted_array[1] += 1
        elif (max_v - min_v) % 2 == (max_v - mid_v) % 2:
            sorted_array[0] += 2
        else:
            sorted_array[1] += 1
            sorted_array[2] += 1
        
        ans += 1

    return ans

a, b, c = map(int, input().split())
print(solve(a, b, c))


print(solve(2, 5, 4) == 2)
print(solve(2, 6, 3) == 5)
print(solve(31, 41, 5) == 23)
