# 1. Create and traverse an array (TC - O(n))
from array import *
my_array = array("i",[1,2,3,4,5,6])
for i in my_array: 
    print(i)

# 2. Access individual elements through indexes (TC - O(1))
print("Step 2")
print(my_array[3])

# 3. Insert an element into the array using append() method - It adds element at the end (TC - O(1))
print("Step 3")
my_array.append(8)
print(my_array)

# 4. Insert value in the array using insert() method (TC - O(n))
print("Step 4")
my_array.insert(0,-1)
print(my_array)

# 5. Extend array using extend() method - Using extend() method we can add another array at the end of the existing array
print("Step 5")
my_array1 = array("i", [7,9,10])
my_array.extend(my_array1)
print(my_array)

# 6. Add items from list into array using fromlist() method
print("Step 6")
lst = [11,12,13]
my_array.fromlist(lst)
print(my_array)

# 7. Remove an element from an array using remove() method (TC - O(n)) - Now if there is an element that is
# repeated in the array, then it will remove the first repeated element
print("Step 7")
my_array.remove(4)
print(my_array)

# 8. Remove last element from an array using pop() method (TC - O(1))
print("Step 8")
my_array.pop()
print(my_array)

# 9. Fetch any element thru its index using index() method
print("Step 9")
print(my_array.index(6))

# 10. Reverse a python array using reverse() method
print("Step 10")
my_array.reverse()
print(my_array)

# 11. Get array buffer info using buffer_info() method - The first parameter says that the array starts from that number in the memory
print("Step 11")
print(my_array.buffer_info())

# 12. Check for number of occurences of an element using count() method
print("Step 12")
my_array.append(12)
print(my_array.count(12))

# 13. Converting array to a python list using tolist() method
print("Step 13")
print(my_array.tolist())

# 14. Slice elements from an array
print("Step 14")
print(my_array[3:7])


