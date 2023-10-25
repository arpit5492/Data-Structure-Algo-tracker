# TC and SC for updating a key inside a dictionary is O(1)
empDetails = {'Name':'Joseph', 'age': 30, 'Address': 'India'}
empDetails['Address'] = 'London'
print(empDetails)

# TC for adding a key is O(1) since all key will get added at the end of the dictionary
# And SC is amortized O(1). It's called amortized because sometimes the computer doesn't know how many keys will be added
empDetails['Id'] = 5632
print(empDetails)
