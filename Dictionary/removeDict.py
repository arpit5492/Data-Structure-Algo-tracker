# There are four methods to delete an element from a dictionary
my_dict = {'Name':'Jimmy', 'Age': 45, 'Address': 'Finland'}
# 1. del --> TC and SC is O(1) since it requires hash table operation
del my_dict['Age']
print(my_dict)

# 2. pop() --> TC and SC is O(1) since it requires hash table operation
# removed_value = my_dict.pop('Address', None)
# print(removed_value)
# print(my_dict)

# 3. popitem() --> TC and SC is O(1) since it requires hash table operation
# print(my_dict.popitem()) # Removes the last lement from the dictionary
# print(my_dict)

# 4. clear() --> TC is O(n) because all the elements will be removed from the dictionary and SC is O(1)
# because no extra space is required to perform this operation
# my_dict.clear()
# print(my_dict)

