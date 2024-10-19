for i in range(20):
    print('im ralph ({})'.format(str(i)))

for x in range(0, 10,3):
    print(x)

for a in range(-5, -1, -1):
    print(a)

for b in [1,2,3,4,5]:
    if b == 6:
        break
else:
    print('only will be print or executed when no one in the list is equal to')

import random
for z in range(5):
    print(random.randint(100000,999999))