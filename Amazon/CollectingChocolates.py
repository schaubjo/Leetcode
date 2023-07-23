def minCost(nums, x):
    N = len(nums)
    # res[k] means the result for k times operation
    # first initialize it to the cost of swapping k times
    res = [x * k for k in range(N)]

    for i in range(N):
        curr = nums[i]
        for k in range(N):
            curr = min(curr, nums[i - k])
            res[k] += curr
    return min(res)


print(minCost([20, 1, 15], 5))
