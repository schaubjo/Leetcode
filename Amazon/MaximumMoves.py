from functools import cache


def maxMoves(grid):
    numRows = len(grid)
    numCols = len(grid[0])

    directions = [(-1, 1), (1, 1), (0, 1)]

    @cache
    def dp(r, c):
        res = 0
        for x, y in directions:
            new_row, new_col = r + x, c + y
            if 0 <= new_row < numRows and new_col < numCols and grid[r][c] < grid[new_row][new_col]:
                res = max(res, 1 + dp(new_row, new_col))

        return res

    maxMoves = 0
    for r in range(numRows):
        maxMoves = max(maxMoves, dp(r, 0))

    return maxMoves


print(maxMoves(grid=[[2, 4, 3, 5], [5, 4, 9, 3],
      [3, 4, 2, 11], [10, 9, 13, 15]]))
