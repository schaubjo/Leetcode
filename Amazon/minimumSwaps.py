def minimumSwaps(nums):
    # find min and max index
    minVal = float('inf')
    minIndex = -1
    maxVal = -1
    maxIndex = -1
    for i in range(len(nums)):
        if nums[i] < minVal:
            minVal = nums[i]
            minIndex = i
        if nums[i] >= maxVal:
            maxVal = nums[i]
            maxIndex = i

    save = 0
    if maxIndex < minIndex:
        save = 1
    rDistance = len(nums) - 1 - maxIndex
    lDistance = minIndex
    return rDistance + lDistance - save


print(minimumSwaps(nums=[3, 4, 5, 5, 3, 1]))
print(minimumSwaps(nums=[9]))
