#Problem: Write a function to compute the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Example usage:
print(factorial(5))  # Output: 120
