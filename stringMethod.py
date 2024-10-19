name = 'hello world'
print(type(name))
print(name[0])
print(name.count('l'))

print(name[0:3])
print(name[:5])
print(name[6:])

print('lo' in name)
print('wor' in name)
print('dave' in name)
print('ralph' not in name)

if 'a' in name:
    print('true')
else:
    print('false')
print(name.upper())
print(name.isupper())
print(name.islower())
print(name.join(['ralp', 'rigor']))
print(name.split())
print(name.split('hell'))
print('ralph'.rjust(20))
print('ralph'.rjust(10, '*'))
print('ralph'.rjust(15, '-'))
print('ralph'.center(30, '-'))
name2 = '     world'
print(name2.strip())
print(name2.rstrip())
name3 = 'john'
age = 20
print(f'my name is {name3} and my age is {age}')

def raiseErr(x):
    if x < 5:
        raise ('less than 5')
    else:
        print('greater than 5')
    
raiseErr(6)

def example_function():
    print("Before raise")
    raise ValueError("An error occurred")
    print("After raise")  # This line will not be executed

try:
    example_function()
except ValueError as e:
    print("Caught ValueError:", e)

add = lambda x,y: x + y
print(add(20,20))
(lambda a, b: a + b) (10, 10)

def makeAdder(n):
    return lambda x: x + n
x = makeAdder(10)
l = makeAdder(15)
print(x(10), l(20))

def addThis(a, b):
    return a + b

print(addThis(50, 50))

# while True:
#     name = input('name: ')
#     if name != 'ralph':
#       print('wrong')
#     else:
#         print('correct')
#         break
num = int(input('num: '))
print(10 + num)

a = 'ralph'
b = 'ralphs'
if a == b:
    print('equal')
else: 
    print('not equal')

