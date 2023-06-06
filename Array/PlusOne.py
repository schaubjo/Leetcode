def plusOne(digits):
    digits[-1] += 1
    if digits[-1] == 10:
        digits[-1] = 0
        carry = 1
        i = len(digits) - 2
        while carry == 1 and i > -1:
            digits[i] += 1
            if digits[i] == 10:
                carry = 1
                digits[i] = 0
            else:
                carry = 0
            i -= 1

        if digits[0] == 10 or digits[0] == 0:
            digits.insert(0, 1)
            digits[1] = 0

    return digits


print(plusOne([1, 2, 3]))
print(plusOne([9]))
