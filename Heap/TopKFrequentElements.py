from collections import Counter
import heapq


def topKFrequent(nums, k):
    counted = Counter(nums)

    bucket = [[] for _ in range(len(nums))]

    for key, val in counted.items():
        bucket[val - 1].append(key)

    res = []
    for i in range(len(bucket) - 1, -1, -1):
        for j in range(len(bucket[i])):
            res.append(bucket[i][j])
            k -= 1
            if k == 0:
                return res

    return res


print(topKFrequent(nums=[1, 1, 1, 1, 2, 2, 3], k=2))
print(topKFrequent(nums=[-1, -1], k=1))
