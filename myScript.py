# name = 'ralph'
# newList = ['ralph', 'rigor', 'santolorin']

# for x in newList:
#     print(x)



class Person:
    def __init__(self, name):
        self.name = name
        # self.speak = speak

    def saySomething(self):
        print('i am the boss ' + ' ' +self.name)   

# person1 = Person('ralph', 'whats up')
# person2 = Person('shenron', 'im shenron')
# person3 = Person('gadwin', 'im gadwin')

# print(person1.saySomething())

# listOfPerson = [person1, person2, person3]

# listOfPerson[1].saySomething()

# for person in listOfPerson:
#   person.saySomething()

listOFpeople = []

for i in range(3):
    name = input('whats person:')
    p = Person(name)
    listOFpeople.append(p)


for people in listOFpeople:
    people.saySomething()