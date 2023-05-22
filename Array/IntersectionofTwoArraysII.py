def intersect(nums1, nums2):
    result = []
    dict1 = {}
    dict2 = {}
    for item in nums1:
        dict1[item] = dict1.get(item, 0) + 1
    for item in nums2:
        dict2[item] = dict2.get(item, 0) + 1

    for key in dict1:
        if key in dict2:
            for i in range(min(dict1[key], dict2[key])):
                result.append(key)

    return result


print(intersect([1, 2, 2, 1], [2, 2]))
