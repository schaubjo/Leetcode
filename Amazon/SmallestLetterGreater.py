def nextGreatestLetter(letters, target):
    targetVal = ord(target) - ord('a')
    smallest = '{'
    found = False
    for i in range(len(letters)):
        currVal = ord(letters[i]) - ord('a')
        if currVal > targetVal and currVal < ord(smallest) - ord('a'):
            smallest = letters[i]
            found = True

    if not found:
        return letters[0]
    else:
        return smallest


print(nextGreatestLetter(letters=["c", "f", "j"], target="a"))
print(nextGreatestLetter(letters=["c", "f", "j"], target="c"))
print(nextGreatestLetter(letters=["x", "x", "y", "y"], target="z"))
