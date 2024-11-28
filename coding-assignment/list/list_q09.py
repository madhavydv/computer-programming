#Problem: Given two lists, return a list of all unique elements from both lists. Solution:

lst1 = [1, 2, 3]
lst2 = [3, 4, 5]
union = list(set(lst1) | set(lst2))
print(union)
