#Problem: Given a list, check if it is a palindrome. Solution:

lst = [1, 2, 3, 2, 1]
is_palindrome = lst == lst[::-1]
print(is_palindrome)
