from collections import Counter
import heapq


def minSetSize(arr):
    numCount = Counter(arr)  # O(n)
    maxHeap = [-1 * v for v in numCount.values()]  # O(n)
    heapq.heapify(maxHeap)  # O(n)

    halfSize = len(arr) // 2
    runningSize = len(arr)
    numRemoved = 0

    while runningSize > halfSize:  # O(n)
        removed = heapq.heappop(maxHeap)  # O(log(n))
        runningSize += removed
        numRemoved += 1

    return numRemoved


print(minSetSize(arr=[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]))
print(minSetSize(arr=[7, 7, 7, 7, 7, 7]))
