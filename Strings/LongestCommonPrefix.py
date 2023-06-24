def longestCommonPrefix(strs):
    curr_idx = 0
    common = True
    longest = ""
    while common:

        if curr_idx < len(strs[0]):
            new_char = strs[0][curr_idx]
        else:
            return longest

        for s in strs:
            if curr_idx == len(s) or s[curr_idx] != new_char:
                return longest

        longest += strs[0][curr_idx]
        curr_idx += 1

    return longest


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix(["dog", "racecar", "car"]))
