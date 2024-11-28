#Problem: Given a number N, return all prime numbers from 1 to N. Solution:

n = 20
primes = []
for i in range(2, n+1):
    if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
        primes.append(i)
print(primes)
