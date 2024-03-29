def rotate(matrix):
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r

            # save the top left value
            topLeft = matrix[top][l + i]

            # move bottom left into top left
            matrix[top][l + i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right into bottom right
            matrix[bottom][r - i] = matrix[top + i][r]

            # move top left into top right
            matrix[top + i][r] = topLeft

        r -= 1
        l += 1




rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
