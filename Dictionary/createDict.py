# TC and SC for creating an empty dictionary is O(1)

dct = dict()
print(dct)
dct1 = {}
print(dct1)

# TC and SC for creating a dictionary with elements in it is O(n)
names = dict(name1 = 'Arpit', name2 = 'Rahul', name3 = 'Rishav')
print(names)
print(names['name2'])

nm = {'name1':'Joseph', 'name2':'John', 'name3': 'Jimmy'}
print(nm)
print(nm['name3'])

# Creating a dictionary using list of tuples

nm1 = [('name1','Tom Cruise'),('name2','Ryan Gosling'),('name3','Murphy')]
diction1 = dict(nm1)
print(diction1)