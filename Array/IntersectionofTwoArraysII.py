def intersect(nums1, nums2):
    result = []
    dict1 = {}
    for item in nums1:
        dict1[item] = dict1.get(item, 0) + 1

    for item in nums2:
        if item in dict1 and dict1[item] > 0:
            result.append(item)
            dict1[item] -= 1

    return result


print(intersect([1, 2, 2, 1], [2, 2]))
