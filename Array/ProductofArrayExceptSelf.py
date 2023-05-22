def productExceptSelf(nums):
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)
    result = []
    for i in range(1, len(nums)):
        prefix[i] = prefix[i - 1] * nums[i - 1]

    for i in range(len(nums) - 2, -1, -1):
        postfix[i] = postfix[i + 1] * nums[i + 1]

    for i in range(len(nums)):
        result.append(prefix[i] * postfix[i])

    return result


productExceptSelf([1, 2, 3, 4])
