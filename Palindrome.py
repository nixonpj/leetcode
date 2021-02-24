def check_palindrome(word):
    if len(word) == 1:
        return True
    elif len(word) == 2:
        return word[0] == word[1]
    elif word[0] != word[-1]:
        return False
    else:
        return check_palindrome(word[1:-1])


# assert check_palindrome("nixon"), False
# assert check_palindrome("malayalam"), True
# assert check_palindrome("heh"), True
# assert check_palindrome("heeh"), True

print(check_palindrome("n33335n"))