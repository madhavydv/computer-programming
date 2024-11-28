#Problem: Check if two strings are anagrams of each other.

s1 = "listen"
s2 = "silent"
if sorted(s1) == sorted(s2):
    print("True")
else:
    print("False")
