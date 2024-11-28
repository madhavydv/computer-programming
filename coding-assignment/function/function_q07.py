#Problem: Write a function to calculate the LCM of two numbers.

def lcm(a, b):
    return a * b // gcd(a, b)

# Example usage:
print(lcm(4, 5))  # Output: 20
