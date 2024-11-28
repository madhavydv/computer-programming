#Write a function that returns the key with the maximum value in a dictionary.

def get_max_key(d):
    return max(d, key=d.get)

dictionary = {'a': 1, 'b': 5, 'c': 3}
print(get_max_key(dictionary))
