def spiralOrder(matrix):
    result = []
    width = len(matrix[0])
    height = len(matrix)
    left, right, top, bottom = 0, 0, 0, 0

    processed = 0
    state = 0
    while processed != width * height:
        if state % 4 == 0:
            for i in range(left, width - right):
                result.append(matrix[top][i])
            top += 1
            processed += width - right - left

        elif state % 4 == 1:
            for i in range(top, height - bottom):
                result.append(matrix[i][width - right - 1])
            right += 1
            processed += height - bottom - top

        elif state % 4 == 2:
            for i in range(width - right - 1, left - 1, -1):
                result.append(matrix[height - bottom - 1][i])
            bottom += 1
            processed += width - right - left

        else:
            for i in range(height - bottom - 1, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
            processed += height - bottom - top

        state += 1

    return result


print(spiralOrder([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [
      15, 16, 17, 18, 19, 20, 21], [22, 23, 24, 25, 26, 27, 28], [29, 30, 31, 32, 33, 34, 35]]))

print(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
