def reverseWords(s):
    words = []
    i = 0
    while i < len(s):
        newWord = ""
        while i < len(s) and not s[i].isspace():
            newWord += s[i]
            i += 1
        if len(newWord) > 0:
            words.append(newWord)
        i += 1

    reversedWords = words[::-1]
    res = ""
    for word in reversedWords:
        res += word
        res += " "
    return res[:-1]


print(reverseWords("the sky is blue"))
