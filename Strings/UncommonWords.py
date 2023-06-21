from collections import Counter


def uncommonFromSentences(s1, s2):
    return [key for key, val in Counter(s1.split() + s2.split()).items() if val == 1]


print(uncommonFromSentences("this apple is sweet", "this apple is sour"))
