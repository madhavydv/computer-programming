#Problem: Write a function that multiplies all elements in a list.

def multiply_elements(lst):
    result = 1
    for num in lst:
        result *= num
    return result

# Example usage:
print(multiply_elements([1, 2, 3, 4]))  # Output: 24
