def minRemoveToMakeValid(s):
    sb = ""
    open = 0

    # getting rid of closing parentheses without a respective opening
    for c in s:
        if c == '(':
            open += 1
        elif c == ')':
            if open == 0:
                continue
            open -= 1
        sb += c

    # now we want to delete any opening parentheses without closing
    res = ""
    for i in range(len(sb) - 1, -1, -1):
        if sb[i] == '(' and open > 0:
            open -= 1
            continue
        res += sb[i]

    return res[::-1]


print(minRemoveToMakeValid("lee(t(c)o)de)"))
print(minRemoveToMakeValid("a)b(c)d"))
print(minRemoveToMakeValid("))(("))
