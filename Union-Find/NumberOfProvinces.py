def findCircleNum(isConnected):
    N = len(isConnected)

    def dfs(r, c):
        if isConnected[r][c] != 1:
            return
        isConnected[r][c] = 0
        for i in range(N):
            dfs(c, i)

    provinces = 0
    for i in range(N):
        for j in range(N):
            if isConnected[i][j] == 1:
                provinces += 1
                dfs(i, j)

    return provinces


print(findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
