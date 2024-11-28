#Problem: Given a list of integers, find the maximum product of two distinct elements. Solution:

lst = [1, 3, 5, 2, 4]
lst.sort()
max_product = lst[-1] * lst[-2]
print(max_product)
