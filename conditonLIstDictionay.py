students = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob', 'age': 21, 'grade': 'B'},
    {'name': 'Charlie', 'age': 22, 'grade': 'C'}
]

for a in students:
    if 'ralph' in a:
        print('Yes, "ralph" key exists in one of the dictionaries')
    else:
        print('No, "ralph" key does not exist in any of the dictionaries')

students = [
    {'name': 'Alice', 'age': 20, 'grade': 'A'},
    {'name': 'Bob', 'age': 21, 'grade': 'B'},
    {'name': 'Charlie', 'age': 22, 'grade': 'C'}
]

for x in students:
    if x['name'] == 'Ralph':
        print('Yes, Ralph is in the list')
    else:
        print('No, Ralph is not in the list')


