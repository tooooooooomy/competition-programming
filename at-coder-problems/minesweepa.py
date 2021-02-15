import copy, math


# Implement your function below.
# n = # rows = # columns in the given 2d array
def rotate(given_array, n):
    for i in range(math.floor(n/2)):
        for j in range(math.ceil(n/2)):
            tmp = [-1, -1, -1, -1]
            c_i, c_j = i, j
            for k in range(4):
                tmp[k] = given_array[c_i][c_j]
                c_i, c_j = rotate_sub(n, c_i, c_j)
            for k in range(4):
                given_array[c_i][c_j] = tmp[(k+3) % 4]
                c_i, c_j = rotate_sub(n, c_i, c_j)

    return given_array
            
def rotate_sub(n, i, j):
    return j, n-i-1

# NOTE: Feel free to use the following function for testing.
# It converts a 2-dimensional array (a list of lists) into
# an easy-to-read string format.
def to_string(given_array):
    list_rows = []
    for row in given_array:
        list_rows.append(str(row))
    return '[' + ',\n '.join(list_rows) + ']'


# NOTE: The following input values will be used for testing your solution.
a1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]
a = rotate(a1, 3)
print(a)
# [[7, 4, 1],
#  [8, 5, 2],
#  [9, 6, 3]]

a2 = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 16]]
# rotate(a2, 4) should return:
# [[13, 9, 5, 1],
#  [14, 10, 6, 2],
#  [15, 11, 7, 3],
#  [16, 12, 8, 4]]

