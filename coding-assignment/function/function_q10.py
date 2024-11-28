#Problem: Write a function that returns the sum of the digits of a number.

def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
print(sum_of_digits(123))  # Output: 6
