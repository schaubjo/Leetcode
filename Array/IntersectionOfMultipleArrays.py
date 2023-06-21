from collections import Counter


def intersection(nums):
    dict1 = Counter(nums[0])
    
    for i in range(1, len(nums)):
        for n in nums[i]:
            if n in dict1:
                dict1[n] += 1

    res = []
    for k, v in dict1.items():
        if v == len(nums):
            res.append(k)

    return sorted(res)
