#Sort a dictionary by its values in ascending order.

dictionary = {'a': 3, 'b': 1, 'c': 2}
sorted_dict = dict(sorted(dictionary.items(), key=lambda item: item[1]))
print(sorted_dict)
