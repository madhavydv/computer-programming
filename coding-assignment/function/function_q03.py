#Problem: Write a function that returns the nth Fibonacci number.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

# Example usage:
print(fibonacci(6))  # Output: 8
