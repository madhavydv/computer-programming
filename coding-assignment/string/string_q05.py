#Problem: Count vowels and consonants in a string.

s = "hello"
vowels = "aeiouAEIOU"
vowels_count = sum(1 for char in s if char in vowels)
consonants_count = sum(1 for char in s if char.isalpha() and char not in vowels)
print("Vowels:", vowels_count)
print("Consonants:", consonants_count)
