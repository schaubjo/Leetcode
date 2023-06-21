# def reverseWords(s):
#     i = 0
#     res = ""
#     while i < len(s):
#         j = i
#         while j < len(s) and s[j] != " ":
#             j += 1
#         word = s[i:j][::-1]
#         res += word + " "
#         i = j + 1

#     return res[:-1]

def reverseWords(s):
    return " ".join(x[::-1] for x in s.split())
    words = s.split()
    rWords = [x[::-1] for x in words]
    return " ".join(rWords)


print(reverseWords("Let's take LeetCode contest"))
