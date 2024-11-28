#Problem: Given a list, rotate it by K positions. Solution:

lst = [1, 2, 3, 4, 5]
k = 2
rotated_lst = lst[-k:] + lst[:-k]
print(rotated_lst)
