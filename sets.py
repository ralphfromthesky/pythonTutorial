# sets no duplcate can eliminate duplicate, unique un order of collection
#can add element

s = {1,2,3,4,5,6,1,2, 'ralph', 'ralph'}
print(s)

#fot update
s.update([7,8,9])
print(s)
#for remove, if remove that there no error it will throw an error
s.remove(4)
print(s)
#for discard, if discard that there no element it will not throw error 
s.discard(5)
#union for comibining
s2 = {'shenron', 'gadwin', 'ralph'}
print(s.union(s2))
#intersection will return only the common or with the same element
s3 = {'ralph'}
print(s.intersection(s2,s3))

a ={1,23,4,5}
print([i - 1 for i in a])

print(type({}))
print('ralph' in s)
