def closedIsland(grid):
    numRows = len(grid)
    numCols = len(grid[0])

    def dfs(r, c):
        if r < 0 or r >= numRows or c < 0 or c >= numCols or grid[r][c] == 1:
            return
        grid[r][c] = 1

        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)

    # top row of grid
    for c in range(numCols):
        dfs(0, c)

    # bottom row
    for c in range(numCols):
        dfs(numRows - 1, c)

    # left col
    for r in range(numRows):
        dfs(r, 0)

    # right col
    for r in range(numRows):
        dfs(r, numCols - 1)

    numIslands = 0
    for r in range(1, numRows - 1):
        for c in range(1, numCols - 1):
            if grid[r][c] == 0:
                numIslands += 1
                dfs(r, c)

    return numIslands


print(closedIsland(grid=[[1, 1, 1, 1, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 1, 0], [
      1, 0, 1, 0, 1, 1, 1, 0], [1, 0, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 1, 1, 0]]))
