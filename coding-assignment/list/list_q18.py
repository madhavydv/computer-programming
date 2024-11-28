#Problem: Given a list and a sum, find two numbers that add up to the given sum. Solution:

lst = [1, 2, 3, 4, 5]
target = 7
seen = set()
pair_found = False
for num in lst:
    if target - num in seen:
        pair_found = True
        break
    seen.add(num)
print(pair_found)
