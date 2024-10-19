#dictionary same like key value pair in javasctipy

myCat = {
    'size': 'fat',
    'color': 'red',
    'age': 10,
    'breed': 'pomeranian'
}
print(myCat)
#for looping values
for a in myCat.values():
    print(a)
#for looping keys
for a in myCat.keys():
    print(a)
#for getting keys an values
for a, b in myCat.items():
    print(f'{a}:{b}')
#for checking the keys boolean
p = 'ralph' in myCat.keys()
print(p)    
#for checking the values bolean
print(10 in myCat.values())
#or you can ommit the keys()
print('age' in myCat)
#use .get()for accessing
print(myCat.get('breed'))
print(myCat['breed'])
#checking if has element and adding
if 'shine' not in myCat:
    myCat['shine'] = 'paula danica mamis'
print(myCat)
#for shortcut if has no element
print(myCat.setdefault('mood', 'angry'))
#for mergin dictionary use **
x ={'a': 1, 'b': 2}
y = {'c': '3', 'd': 4}
z = {**x, **y}
print(z)

if 'dave' in myCat:
    print('it has')
else:
    print('nothing')
    
fruits = {
    'banana': 10,
    'apple': 20
}

for a, b in fruits.items():
    print(f'{a} - {b}')

print(fruits['apple'])