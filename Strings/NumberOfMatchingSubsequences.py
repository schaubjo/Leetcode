from collections import defaultdict


def numMatchingSubseq(s, words):
    # create dict for s with val being a list of indices
    lookup = defaultdict(list)

    for i, c in enumerate(s):
        lookup[c].append(i)

    def binary_search(index_list, i):
        l, r = 0, len(index_list)
        while l < r:
            mid = (l + r) // 2
            if i < index_list[mid]:
                r = mid
            else:
                l = mid + 1

        return l

    for word in words:
        prev = -1
        found = True
        for c in word:
            tmp = binary_search(lookup[c], prev)
            if tmp == len(lookup[c]):
                found = False
                break
            else:
                prev = lookup[c][tmp]
        
        if found:


print(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
