def solve(board):
    ROWS = len(board)
    COLS = len(board[0])

    def dfs(r, c):
        if (r < 0 or c < 0 or r == ROWS or
                c == COLS or board[r][c] != 'O'):
            return

        board[r][c] = 'T'
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    # Capture unsurrounded regions

    for r in range(ROWS):
        for c in range(COLS):
            # if we are on the edge of the board and it's O, we capture
            if (board[r][c] == 'O' and (r in [0, ROWS - 1]
                                        or c in [0, COLS - 1])):
                dfs(r, c)

    # Capture surrounded regions
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'O':
                board[r][c] = 'X'

    # Convert T's back to O's
    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == 'T':
                board[r][c] = 'O'
