def isAlienSorted(words, order):
    order_dict = {}
    for i, c in enumerate(order):
        order_dict[c] = i

    def pairSorted(w1, w2):
        p1, p2 = 0, 0
        while p1 < len(w1) and p2 < len(w2):
            if order_dict[w1[p1]] < order_dict[w2[p2]]:
                return True
            elif order_dict[w1[p1]] > order_dict[w2[p2]]:
                return False
            else:
                p1, p2 = p1 + 1, p2 + 1

        if p1 == len(w1):
            return True
        else:
            return False

    for i in range(len(words) - 1):
        j = i + 1
        if pairSorted(words[i], words[j]):
            continue
        else:
            return False

    return True


print(isAlienSorted(words=["hello", "leetcode"],
      order="hlabcdefgijkmnopqrstuvwxyz"))
print(isAlienSorted(words=["word", "world", "row"],
      order="worldabcefghijkmnpqstuvxyz"))
print(isAlienSorted(words=["apple", "app"],
      order="abcdefghijklmnopqrstuvwxyz"))
