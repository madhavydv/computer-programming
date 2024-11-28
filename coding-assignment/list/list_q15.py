#Problem: Given a list of lists, flatten it into a single list. Solution:

lst = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in lst for item in sublist]
print(flattened)
