#How do you check if a key exists in a dictionary before accessing it?

my_dict = {'a': 1, 'b': 2}
if 'c' in my_dict:
    print(my_dict['c'])
else:
    print("Key not found")
