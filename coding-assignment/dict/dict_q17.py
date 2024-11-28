#Access values in a nested dictionary.

students = {
    'student1': {'name': 'Alice', 'age': 25, 'major': 'Computer Science'},
    'student2': {'name': 'Bob', 'age': 23, 'major': 'Mathematics'}
}
# Access value in nested dictionary
student1_name = students['student1']['name']
print(student1_name) 
