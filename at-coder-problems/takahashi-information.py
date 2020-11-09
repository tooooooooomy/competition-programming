def solve(c):
    max_a1 = max(c[0])
    max_a2 = max(c[1])
    max_a3 = max(c[2])
    max_b1 = max(c[0][0], c[1][0], c[2][0])
    max_b2 = max(c[0][1], c[1][1], c[2][1])
    max_b3 = max(c[0][2], c[1][2], c[2][2])

    a1 = 0
    while a1 <= max_a1:
        a2 = 0
        while a2 <= max_a2:
            a3 = 0
            while a3 <= max_a3:
                b1 = 0
                while b1 <= max_b1:
                    b2 = 0
                    while b2 <= max_b2:
                        b3 = 0
                        while b3 <= max_b3:
                            if c[0][0] == a1 + b1 and c[0][1] == a1 + b2 and c[0][2] == a1 + b3 and c[1][0] == a2 + b1 and c[1][1] == a2 + b2 and c[1][2] == a2 + b3 and c[2][0] == a3 + b1 and c[2][1] == a3 + b2 and c[2][2] == a3 + b3:
                                    return 'Yes'
                            b3 += 1
                        b2 += 1
                    b1 += 1
                a3 += 1
            a2 += 1
        a1 += 1

    return 'No'


print(solve([[1, 0, 1], [2, 1, 2], [1, 0, 1]]) == 'Yes')
print(solve([[2, 2, 2], [2, 1, 2], [2, 2, 2]]) == 'No')
print(solve([[0, 8, 8], [0, 8, 8], [0, 8, 8]]) == 'Yes')
print(solve([[1, 8, 6], [2, 9, 7], [0, 7, 7]]) == 'No')
