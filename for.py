listed =  [12,3,5,77,8,12, 1,23,123,45,6,777, 'ralph']

# for i in range(10):
#     print(i)
    
# for i in range(10, -1, -1):
#     print(i)
    
# for i in listed:
#     print(i)

for i, e in enumerate(listed):
    print(i + 1, e)

if('ralphs' in listed):
    print('yes it has the word "ralph"')
else:
    print('no its not')