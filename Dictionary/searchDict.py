my_dict = {'Name':'Jimmy', 'Age': 45, 'Address': 'Finland'}
def searchDict(dict, target):
    for k in dict: # ------> O(n)
        if dict[k] == target: # -----> O(1)
            return k,target # ----> O(1)
    return "The value doesn't exist" # ----> O(1)
print(searchDict(my_dict, 'Finland'))

# TC -> O(n)
# SC -> O(1)