#Problem: Swap two elements in a tuple.
#Example: (1, 2, 3, 4), swap 2 and 4 → (1, 4, 3, 2)

t = (1, 2, 3, 4)
t = (t[0], t[3], t[2], t[1])
print(t)
