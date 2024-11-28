#Problem: Implement the Knuth-Morris-Pratt (KMP) string matching algorithm.

text = "hello"
pattern = "ll"
lps = [0] * len(pattern)
length = 0
i = 1
while i < len(pattern):
    if pattern[i] == pattern[length]:
        length += 1
        lps[i] = length
        i += 1
    else:
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1
i = 0
j = 0
while i < len(text):
    if pattern[j] == text[i]:
        i += 1
        j += 1
    if j == len(pattern):
        print(i - j)
        break
    elif i < len(text) and pattern[j] != text[i]:
        if j != 0:
            j = lps[j - 1]
        else:
            i += 1
else:
    print(-1)
