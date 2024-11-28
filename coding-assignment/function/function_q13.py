#Problem: Write a function that counts how many times an element occurs in a list.

def count_occurrences(lst, x):
    return lst.count(x)

# Example usage:
print(count_occurrences([1, 2, 3, 4, 2, 2], 2))  # Output: 3
