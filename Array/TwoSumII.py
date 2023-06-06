def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum > target:
            r -= 1
        elif sum < target:
            l += 1
        else:
            return l + 1, r + 1
    return -1


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([2, 3, 4], 6))
print(twoSum([-1, 0], -1))
