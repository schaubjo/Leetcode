def lengthOfLongestSubstring(s):
    seen = set()
    maxLength = 0
    runningLength = 0
    slow = 0
    for i in range(len(s)):
        while s[i] in seen:
            seen.remove(s[slow])
            slow += 1
            runningLength -= 1

        seen.add(s[i])
        runningLength += 1
        maxLength = max(maxLength, runningLength)

    return maxLength


print(lengthOfLongestSubstring(s="abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
