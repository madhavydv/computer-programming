#Given two lists, create a dictionary where one list contains the keys and the other contains the values.

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict = dict(zip(keys, values))
print(res_dict)
