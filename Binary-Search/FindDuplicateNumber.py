def findDuplicate(nums):
    slow, fast = 0, 1
    while True:
        slow = (slow + nums[slow]) % len(nums)
        fast = (fast + nums[fast]) % len(nums)
        fast = (fast + nums[fast]) % len(nums)
    return nums[slow]


print(findDuplicate(nums=[1, 3, 4, 2, 2]))
print(findDuplicate(nums=[3, 1, 3, 4, 2]))
