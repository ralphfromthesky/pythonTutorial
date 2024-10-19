#aribitraty, use * as parameter you can pass many arguments as you like
def manyArgs(*args):
    for a in args:
        print(a)
        
manyArgs('ralph', 'rigor', 'santolorin')

#kwargs or keywornd arguments you can pass as many key value pairs
def manyKeyValuePairs(**anoNA):
    for a, b in anoNA.items():
        print(f'this is the key - {a} and this is the values - {b}')
        
manyKeyValuePairs(name='ralph', lastName='santolorin')