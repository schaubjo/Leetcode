def findRedundantConnection(edges):
    N = len(edges)
    parent = [i for i in range(N + 1)]
    rank = [1] * (N + 1)

    def find(n):
        p = parent[n]
        while p != parent[p]:
            p = parent[p]

        # path compression
        q = n
        while q != p:
            next = parent[q]
            parent[q] = p
            q = next
        return p

    def union(n1, n2):
        p1, p2 = find(n1), find(n2)

        if p1 == p2:
            return False

        if rank[p1] > rank[p2]:
            parent[p2] = p1
            rank[p1] += rank[p2]
        else:
            parent[p1] = p2
            rank[p2] += rank[p1]
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return n1, n2


print(findRedundantConnection([[1, 2], [1, 3], [2, 3]]))
