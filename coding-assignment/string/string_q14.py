#Problem: Check if two strings are isomorphic.

s1 = "egg"
s2 = "add"
if len(s1) != len(s2):
    print("False")
else:
    mapping = {}
    for a, b in zip(s1, s2):
        if a not in mapping:
            mapping[a] = b
        elif mapping[a] != b:
            print("False")
            break
    else:
        print("True")
