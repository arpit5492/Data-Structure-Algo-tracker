mylist = [10,20,30,40,50,60,70,80,90]
target = 80
# Search using in operator

# def inSearch(lst, t):
#     if t in lst:
#         print(f"{t} is in the list")
#     else:
#         print(f"{t} is not in the list")
# inSearch(mylist, target)

# Linear search

def linear_search(lst, t):
    for i, value in enumerate(lst):
        if value == t:
            return i
    return -1

print(linear_search(mylist, target))
