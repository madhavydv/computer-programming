#Problem: Remove all duplicate characters in a string.
#Example: "aabcc" → "abc"
s = "aabcc"
print("".join(sorted(set(s), key=s.index)))
