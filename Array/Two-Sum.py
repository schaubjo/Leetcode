def twoSum(nums, target):
    nums_dict = {}
    for i, num in enumerate(nums):
        if target - num in nums_dict:
            return nums_dict[target - num], i
        else:
            nums_dict[num] = i

    return -1


print(twoSum([2, 7, 11, 15], 9))

print(twoSum([3, 2, 4], 6))

print(twoSum([3, 3], 6))
