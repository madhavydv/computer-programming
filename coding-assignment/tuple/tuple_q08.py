#Problem: Concatenate two tuples and then sort the resulting tuple.

t1 = (1, 2, 3)
t2 = (4, 5, 6)
sorted_tuple = tuple(sorted(t1 + t2))
print(sorted_tuple)
