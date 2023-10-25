my_dict = {'Name':'Jimmy', 'Age': 45, 'Address': 'Finland'}
def traverseDict(dict):
    for k in dict: # -----> O(n)
        print(k,dict[k]) # -----> O(1)
traverseDict(my_dict)

# TC -> O(n)
# SC -> O(1)