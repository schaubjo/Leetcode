def threeSum(nums):

    # sort input array
    nums.sort()

    res = []
    for a in range(len(nums)):
        if a > 0 and nums[a - 1] == nums[a]:
            continue
        b = a + 1
        c = len(nums) - 1

        while b < c:
            threeSum = nums[a] + nums[b] + nums[c]
            if threeSum < 0:
                b += 1
            elif threeSum > 0:
                c -= 1
            else:
                res.append([nums[a], nums[b], nums[c]])
                b += 1
                while nums[b] == nums[b - 1] and b < c:
                    b += 1

    return res


print(threeSum(nums=[-1, 0, 1, 2, -1, -4]))
