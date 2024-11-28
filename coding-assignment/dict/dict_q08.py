#Given a list of elements, use a dictionary to count the frequency of each element.

lst = ['a', 'b', 'a', 'c', 'a', 'b']
freq_dict = {}
for item in lst:
    freq_dict[item] = freq_dict.get(item, 0) + 1
print(freq_dict)
