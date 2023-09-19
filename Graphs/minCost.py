def minCostConnectPoints(points):
    # manhattan distance calculator
    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    visited = [False for _ in range(len(points))]
    dist = [float('inf') for _ in range(len(points))]
    parent = [i for i in range(len(points))]

    # start at root node
    dist[0] = 0
    totalCost = 0
    for i in range(len(visited)):
        # find node to start with
        minDist = float('inf')
        curr = 0
        for j in range(len(visited)):
            if not visited[j] and dist[j] < minDist:
                minDist = dist[j]
                curr = j

        # set node to True
        visited[curr] = True

        # add to total
        totalCost += dist[curr]

        # update distances of all False nodes
        for j in range(len(visited)):
            if not visited[j]:
                newDistance = distance(points[j], points[curr])

                # update parent if shorter edge found
                if newDistance < dist[j]:
                    dist[j] = newDistance
                    parent[j] = curr

    return totalCost


print(minCostConnectPoints(points=[[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]))
print(minCostConnectPoints(points=[[3, 12], [-2, 5], [-4, 1]]))
