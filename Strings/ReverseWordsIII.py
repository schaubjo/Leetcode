def reverseWords(s):
    i = 0
    res = ""
    while i < len(s):
        j = i
        while j < len(s) and s[j] != " ":
            j += 1
        word = s[i:j][::-1]
        res += word + " "
        i = j + 1

    return res[:-1]


print(reverseWords("Let's take LeetCode contest"))
