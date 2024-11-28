#Problem: Write a function to calculate the GCD of two numbers.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage:
print(gcd(56, 98))
