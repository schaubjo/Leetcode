from collections import Counter
import heapq


def topKFrequent(nums, k):
    counted = Counter(nums)

    priority_queue = []
    for key, val in counted.items():
        heapq.heappush(priority_queue, (-1 * val, key))

    res = []
    for i in range(k):
        res.append(heapq.heappop(priority_queue)[1])

    return res


print(topKFrequent(nums=[1, 1, 1, 1, 2, 2, 3], k=2))
print(topKFrequent(nums=[-1, -1], k=1))
