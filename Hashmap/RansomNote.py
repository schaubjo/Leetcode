from collections import Counter


def canConstruct(ransomNote, magazine):
    magDict = Counter([*magazine])
    for c in ransomNote:
        if c not in magDict or magDict[c] == 0:
            return False
        else:
            magDict[c] -= 1

    return True


print(canConstruct(ransomNote="a", magazine="b"))
print(canConstruct(ransomNote="aa", magazine="ab"))
print(canConstruct(ransomNote="aa", magazine="aab"))
