#aribitraty, use * as parameter you can pass many arguments as you like
def manyArgs(*whar):
    for a in whar:
        print(a)
        
manyArgs('ralph', 'rigor', 'santolorin', 'shenron', 'gadwin')

#kwargs or keywornd arguments you can pass as many key value pairs
# def manyKeyValuePairs(**anoNA):
#     for a, b in anoNA.items():
#         print(f'this is the key - {a} and this is the values - {b}')
        
# manyKeyValuePairs(name='ralph', lastName='santolorin')

def addNum(a, b):
    return a + b
a = addNum(10, 20)
print(a)