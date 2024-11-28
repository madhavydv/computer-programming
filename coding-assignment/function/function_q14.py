#Problem: Write a function that computes the sum of all even numbers from 1 to n.

def sum_of_evens(n):
    return sum(i for i in range(2, n + 1, 2))

# Example usage:
print(sum_of_evens(10))  # Output: 30

