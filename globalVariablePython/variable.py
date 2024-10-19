my_list = [1, 2, 3]
my_dict = {"name": "John", "age": 30}

# Using append() method to add dictionary to the end of the list
my_list.append(my_dict)

# Using insert() method to add dictionary at a specific index
my_list.insert(0, my_dict)

# for list in my_dict.values():
#     print(list)
    
object = {
    'person ' : {'name': 'ralph'}
}

for a in object:
    print(object[a]['name'])
    
my_tuple = (1,2,3,4,5)
new = my_tuple[1]
print(new)

new_tuple = my_tuple + (4,5,6,8,9)  # Concatenating my_tuple with a new tuple containing the element 4
print(new_tuple)

newYup = (9,9,9,9,)

N = my_tuple + newYup
print(N)