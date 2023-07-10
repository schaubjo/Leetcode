def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
        sum = numbers[l] + numbers[r]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return [l + 1, r + 1]


print(twoSum(numbers=[2, 3, 4], target=6))
print(twoSum(numbers=[-1, 0], target=-1))
