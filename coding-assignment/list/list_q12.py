#Problem: Given a list of integers from 1 to N with one missing number, find the missing number. Solution:

lst = [1, 2, 4, 5]
n = len(lst) + 1
total_sum = n * (n + 1) // 2
missing_number = total_sum - sum(lst)
print(missing_number)
