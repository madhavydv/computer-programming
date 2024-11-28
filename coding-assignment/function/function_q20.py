#Problem: Write a function that finds the common elements between two lists.

def common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Example usage:
print(common_elements([1, 2, 3], [2, 3, 4]))  # Output: [2, 3]
