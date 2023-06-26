def validPalindrome(s):
    def palindrome(s):
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True

    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return palindrome(s[l + 1:r + 1]) or palindrome(s[l:r])
        l, r = l + 1, r - 1
    return True


print(validPalindrome("aba"))
print(validPalindrome("abca"))
print(validPalindrome("abc"))
