def longestConsecutive(nums):
    # turn array into set
    numSet = set(nums)
    longest = 0
    for n in nums:
        # if it's not the start of consecutive numbers, don't count
        if n - 1 in numSet:
            continue
        else:
            c = n
            newLongest = 0
            while c in numSet:
                newLongest += 1
                c += 1
            longest = max(longest, newLongest)

    return longest


print(longestConsecutive([100, 4, 200, 1, 3, 2]))
