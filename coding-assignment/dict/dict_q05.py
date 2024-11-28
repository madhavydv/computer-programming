#Remove a list of keys from a dictionary.

sample_dict = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
keys_to_remove = ['Ten', 'Thirty']
for key in keys_to_remove:
    del sample_dict[key]
print(sample_dict)
