import heapq


def kClosest(points, k):
    def euclidean(x, y):
        return x ** 2 + y ** 2

    minHeap = [(euclidean(p[0], p[1]), p) for p in points]

    heapq.heapify(minHeap)
    return [heapq.heappop(minHeap)[1] for i in range(k)]


print(kClosest(points=[[1, 3], [-2, 2]], k=1))
