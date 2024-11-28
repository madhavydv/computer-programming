#Use dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of the keys.

squares = {x: x**2 for x in range(1, 11)}
print(squares)
