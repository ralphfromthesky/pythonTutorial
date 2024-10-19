class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print('my name is ' + self.name + 'my age is ' + str(self.age))