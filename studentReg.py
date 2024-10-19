class person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location
    
    def myLocation(self):
        print('my name is ' + ' '+ self.name)
        print('my age is ' + ' '+ self.age)
        print('my location is ' + ' '+ self.location)




listOfPerson = []

while True: 
    print()
    name = input('name:')
    age = input('age:')
    location = input('location:')
    choice = input('add another? [y/n]:')
    s = person(name, age, location)
    listOfPerson.append(s)
    print()
    if choice == 'y' or choice == 'Y': pass
    else: break

i = 1
for pers in listOfPerson:
    print('person no.' + str(i))
    i = i + 1
    pers.myLocation()
    print()