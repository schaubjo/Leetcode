def lengthOfLongestSubstring(s):
    letters = set()
    l = 0
    res = 0
    for r in range(len(s)):
        while s[r] in letters:
            letters.remove(s[l])
            l += 1
        letters.add(s[r])
        res = max(res, len(letters))
    return res


print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
