def setZeroes(matrix):
    row_zero = 1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                matrix[0][col] = 0
                if row == 0:
                    row_zero = 0
                else:
                    matrix[row][0] = 0

    for row in range(1, len(matrix)):
        for col in range(1, len(matrix[0])):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0

    if matrix[0][0] == 0:
        for row in range(len(matrix)):
            matrix[row][0] = 0

    if row_zero == 0:
        for col in range(len(matrix[0])):
            matrix[0][col] = 0


setZeroes([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])
