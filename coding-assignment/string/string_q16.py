#Problem: Check if one string is a rotation of another.

s1 = "waterbottle"
s2 = "erbottlewat"
if len(s1) == len(s2) and s2 in (s1 + s1):
    print("True")
else:
    print("False")
