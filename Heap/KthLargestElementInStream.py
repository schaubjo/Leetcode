import heapq


class KthLargest:

    def __init__(self, k, nums):
        # min heap with k largest integers
        self.minHeap, self.k = nums, k

        # heapify our input array
        heapq.heapify(self.minHeap)

        # pop elements until we only have k elements in heap
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        # add element onto heap
        heapq.heappush(self.minHeap, val)

        # now we have k + 1 elements, but we want the k largest
        # so we will pop the minimum element

        # our min heap might have less than k elements already, so
        # we only want to pop if we have greater than k elements
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)

        # kth largest value will be the minimum or index 0
        return self.minHeap[0]
