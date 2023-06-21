def reverseWords(s):
    i = 0
    res = ""
    while i < len(s):
        while i < len(s) and s[i] == ' ':
            i += 1
        j = i + 1
        while j < len(s) and s[j] != ' ':
            j += 1
        word = s[i:j]

        if len(word) > 0 and not word.isspace():
            res = word + " " + res if len(res) > 0 else word

        i = j + 1

    return res


print(reverseWords("  hello world  "))
