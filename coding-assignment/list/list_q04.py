#Problem: Given a list of integers, find the second largest element. Solution:

lst = [1, 3, 2, 5, 4]
unique_lst = list(set(lst))
unique_lst.sort()
second_largest = unique_lst[-2] if len(unique_lst) > 1 else None
print(second_largest)
