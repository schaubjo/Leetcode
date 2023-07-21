def convert(s, numRows):
    if numRows == 1:
        return s

    resList = []
    for r in range(numRows):
        increment = (numRows - 1) * 2
        for i in range(r, len(s), increment):
            resList.append(s[i])
            # middle rows
            if r > 0 and r < numRows - 1 and i + increment - 2 * r < len(s):
                resList.append(s[i + increment - 2 * r])

    # convert back to a string
    return "".join(resList)
