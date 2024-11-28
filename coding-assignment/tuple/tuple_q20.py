#Problem: Find the sum of elements at even indices of a tuple.

t = (1, 2, 3, 4, 5)
print(sum(t[i] for i in range(0, len(t), 2)))
