import heapq


def findKthLargest(nums, k):
    maxHeap = [-1 * n for n in nums]
    heapq.heapify(maxHeap)
    for i in range(k - 1):
        heapq.heappop(maxHeap)

    return maxHeap[0] * -1


print(findKthLargest(nums=[3, 2, 1, 5, 6, 4], k=2))
