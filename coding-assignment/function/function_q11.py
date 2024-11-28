#Problem: Write a function to check if a number is a perfect number.

def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# Example usage:
print(is_perfect(6))  # Output: True
print(is_perfect(28)) # Output: True
