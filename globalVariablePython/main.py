# IMPORTING GLOBAL FUNCTION OR VARIABLE
import arithmethicGlobal
import variable
import classVariable
import tradeTest.bs.importingGlobal

#use 'as' for shortcut name, example: import arithmethicGlobal as a
# import arithmethicGlobal as a

#use 'from' key word for importing a certain variable or function
# from arithmethicGlobal import add as t


print(arithmethicGlobal.add(10, 10))
arithmethicGlobal.minus(10, 1)
arithmethicGlobal.divide(10, 2)
arithmethicGlobal.times(5, 5)

print(variable.name + ' ' + str(variable.number))

newStudent = classVariable.person('ralph', 30)
newStudent.introduce()




#global variabele
y= 'world'

#local variable
def sayhello():
    x = 'hello'
    print(x  + y)
    
sayhello()

#parameter variable

def sayWhat(word):
    print(word)
    
sayWhat('ano na?')

#global keyword

def anoNa():
    global y #for refferencing global variable
    y = 'ano daw?'
    print(y)
    
anoNa()

