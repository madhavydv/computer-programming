#Problem: Given two lists, return a list of elements that appear in both lists. Solution:

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
intersection = list(set(lst1) & set(lst2))
print(intersection)
