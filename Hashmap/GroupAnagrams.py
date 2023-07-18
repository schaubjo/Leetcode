from collections import defaultdict


def groupAnagrams(strs):
    res = defaultdict(list)

    for s in strs:
        charCount = [0] * 26
        for c in s:
            charCount[ord(c) - ord('a')] += 1

        res[tuple(charCount)].append(s)

    return res.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
