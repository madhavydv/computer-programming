#Problem: Print all possible substrings of a string.

s = "abc"
for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        print(s[i:j])
