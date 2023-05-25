def rotate(nums, k):

    k %= len(nums)
    # reverse entire array
    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    # reverse first k elements
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    # reverse last k elements
    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1

    print(nums)


rotate([1, 2, 3, 4, 5, 6, 7], 3)
rotate([-1, -100, 3, 99], 2)
