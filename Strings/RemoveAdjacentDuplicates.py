def removeDuplicates(s):
    char_stack = []
    for c in s:
        if len(char_stack) > 0 and char_stack[-1] == c:
            char_stack.pop()
        else:
            char_stack.append(c)

    return "".join(char_stack)


print(removeDuplicates("abbaca"))
print(removeDuplicates("azxxzy"))
