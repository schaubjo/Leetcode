def romanToInt(s):
    translate = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}

    curr, next = 0, 1
    res = 0
    while next < len(s):
        if translate[s[curr]] >= translate[s[next]]:
            res += translate[s[curr]]
            curr += 1
            next += 1
        else:
            res += translate[s[next]] - translate[s[curr]]
            curr += 2
            next += 2

    if curr < len(s):
        res += translate[s[curr]]

    return res


print(romanToInt("III"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
