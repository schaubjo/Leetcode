from collections import Counter
from math import ceil


def minimumRounds(tasks):
    diffDict = Counter(tasks)
    numRounds = 0
    for v in diffDict.values():
        if v == 1:
            return -1
        numRounds += ceil(v / 3)

    return numRounds


print(minimumRounds(tasks=[2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
print(minimumRounds(tasks=[2, 3, 3]))
