def stringpalindrome(str):
    str = str.replace(" ","").lower()
    reversed = str[::-1]
    if reversed == str:
        return f"string {str} is palindrome. "
    else:
        return f"string {str} is not palindrome. "

output = stringpalindrome("A man a plan a canal Panama")
print(output)