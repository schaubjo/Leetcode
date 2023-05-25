def rotate(nums, k):

    def reversal(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

    k %= len(nums)
    # reverse entire array
    reversal(0, len(nums) - 1)

    # reverse first k elements
    reversal(0, k - 1)

    # reverse last k elements
    reversal(k, len(nums) - 1)

    print(nums)


rotate([1, 2, 3, 4, 5, 6, 7], 3)
rotate([-1, -100, 3, 99], 2)
