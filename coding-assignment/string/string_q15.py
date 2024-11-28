#Problem: Find the first non-repeating character in a string.

s = "leetcode"
for char in s:
    if s.count(char) == 1:
        print(char)
        break
else:
    print(None)
