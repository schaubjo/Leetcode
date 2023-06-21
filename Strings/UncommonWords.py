from collections import Counter


def uncommonFromSentences(s1, s2):
    dict1, dict2 = Counter(s1.split()), Counter(s2.split())
    res = []
    for key, val in dict1.items():
        if val == 1 and key not in dict2:
            res.append(key)
    for key, val in dict2.items():
        if val == 1 and key not in dict1:
            res.append(key)

    return res


print(uncommonFromSentences("this apple is sweet", "this apple is sour"))
