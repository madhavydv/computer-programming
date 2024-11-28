#Problem: Write a function that checks if a number is prime.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Example usage:
print(is_prime(7))  # Output: True
print(is_prime(10)) # Output: False
