def search(nums, target):
    left = 0
    right = len(nums) - 1
    while (left <= right):
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle
        # left portion
        if nums[middle] >= nums[left]:
            # we can cut off the left sorted portion because it would have to be in the right
            if target < nums[left]:
                left = middle
        # right portion
        else:
