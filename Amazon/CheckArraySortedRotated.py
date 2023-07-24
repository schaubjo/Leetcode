def check(nums):
    breaks = 0
    for i in range(len(nums)):
        if nums[i] < nums[i - 1]:
            breaks += 1
    return breaks <= 1


print(check(nums=[3, 4, 5, 1, 2]))
print(check(nums=[2, 1, 3, 4]))
print(check(nums=[1, 2, 3]))
print(check(nums=[6, 10, 6]))
