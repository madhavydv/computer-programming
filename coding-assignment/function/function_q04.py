#Problem: Write a function that checks if a string is a palindrome.

def is_palindrome(s):
    return s == s[::-1]

# Example usage:
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
