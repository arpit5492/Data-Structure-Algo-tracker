import numpy as np
TwoDimArray = np.array([[1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12],
                        [13,14,15,16]])
print(TwoDimArray)

newArr = np.delete(TwoDimArray, 1, axis=1)
print(newArr)