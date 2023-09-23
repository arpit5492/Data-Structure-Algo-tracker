import array

arr1=array.array('i',[1,2,3,4,5,6])
def accessElement(array,index):
    if index >= len(array):
        print("There is no element in the index")
    else:
        print(array[index])
accessElement(arr1,5)