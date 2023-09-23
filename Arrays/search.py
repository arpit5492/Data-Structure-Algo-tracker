import array
arr1=array.array('i',[1,2,3,4,5,6])

def search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            return i
    return -1
print(search(arr1,6))