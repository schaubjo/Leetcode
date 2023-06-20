def lengthOfLongestSubstring(s):
    letters = set()
    start = 0
    longest = 0
    for c in range(len(s)):
        if s[c] in letters:
            longest = max(c - start, longest)
            start = c
        else:
            letters.add(s[c])

    return
