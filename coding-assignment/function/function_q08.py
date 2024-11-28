#Problem: Write a function that counts the number of vowels in a string.

def count_vowels(s):
    vowels = "aeiou"
    return sum(1 for char in s if char in vowels)

# Example usage:
print(count_vowels("hello"))  # Output: 
