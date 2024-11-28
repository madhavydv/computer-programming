#Problem: Find the longest common prefix in a list of strings.

strs = ["flower", "flow", "flight"]
prefix = strs[0]
for string in strs[1:]:
    while not string.startswith(prefix):
        prefix = prefix[:-1]
print(prefix)
