#Find the key with the minimum value in a dictionary.

def get_min_key(d):
    return min(d, key=d.get)
dictionary = {'a': 3, 'b': 1, 'c': 5}
print(get_min_key(dictionary))  # Output: 'b'
