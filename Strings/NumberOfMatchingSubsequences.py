from collections import defaultdict
import bisect


def numMatchingSubseq(s, words):
<<<<<<< HEAD
    # create dict for s with val being a list of indices
    lookup = defaultdict(list)

    for i, c in enumerate(s):
        lookup[c].append(i)
=======
        # create dict for s with val being a list of indices
        lookup = defaultdict(list)
>>>>>>> test1

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

<<<<<<< HEAD
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
=======
            return l

        count = 0
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
                count += 1

        return count
>>>>>>> test1


print(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))
