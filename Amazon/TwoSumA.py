def twoSum(nums, target):
    numsDict = {}  # val -> index
    for i in range(len(nums)):
        if target - nums[i] in numsDict:
            return i, numsDict[target - nums[i]]
        else:
            numsDict[nums[i]] = i

    return
