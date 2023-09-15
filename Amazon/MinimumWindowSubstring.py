from collections import deque


def minWindow(s, t):
    if len(t) > len(s):
        return ""

    tDict = {}
    # create dict for occurrences in t
    for c in t:
        tDict[c] = tDict.get(c, 0) + 1
    sDict = {}
    indices = deque()
    res = s + 'p'
    found = False
    for i in range(len(s)):
        if s[i] in tDict:

            indices.append(i)
            # pop off elements until dict occurrences are equal
            sDict[s[i]] = sDict.get(s[i], 0) + 1
            while sDict[s[i]] > tDict[s[i]]:
                popped = indices.popleft()
                sDict[s[popped]] -= 1

            if sDict == tDict and (indices[-1] - indices[0] + 1 < len(res)):
                res = s[indices[0]:indices[-1]+1]
                found = True

    return res if found else ""


print(minWindow(s="ADOBECODEBANC", t="ABC"))
print(minWindow(s="a", t="a"))
print(minWindow(s="a", t="aa"))
print(minWindow(s="ab", t="aa"))
