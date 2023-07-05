def findCircleNum(isConnected):
    N = len(isConnected)
    parent = [i for i in range(N)]
    rank = [1] * (N)

    def find(n):
        p = parent[n]
        while parent[p] != p:
            p = parent[p]

        # p is now the root representative

        # path compression
        q = n
        while parent[q] != p:
            next = parent[q]
            parent[q] = p
            q = next

        # return the root that we found
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]

        else:
            parent[p1] = p2
            rank[p2] += rank[p1]

    # union everything together
    ROWS = len(isConnected)
    COLS = len(isConnected[0])

    for i in range(ROWS):
        for j in range(COLS):
            if isConnected[i][j] == 1 and i != j and parent[i] != parent[j]:
                union(i, j)

    count = 0
    for i in range(len(parent)):
        if parent[i] == i:
            count += 1

    return count


print(findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
