def partitionString(s):
    charSet = set()
    numPartitions = 1
    for i in range(len(s)):
        if s[i] not in charSet:
            charSet.add(s[i])
        else:
            charSet.clear()
            charSet.add(s[i])
            numPartitions += 1

    return numPartitions


print(partitionString(s="abacaba"))
print(partitionString(s="ssssss"))
