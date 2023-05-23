def MajorityElement(nums):
    count = {}
    result = 0
    maxCount = 0
    for i in nums:
        count[i] = 1 + count.get(i, 0)
        result = i if count[i] > maxCount else result
        maxCount = max(maxCount, count[i])

    return result
