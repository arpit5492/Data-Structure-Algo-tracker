import numpy as np
TwoDimArray = np.array([[1,2,3,4],
                        [5,6,7,8],
                        [9,10,11,12],
                        [13,14,15,16]])
print(TwoDimArray)

# newArray = np.insert(TwoDimArray, 2, [[-1,-2,-3,-4]], axis=0)
# print(newArray)

newArray = np.append(TwoDimArray, [[56,57,58,49]], axis=0)
print(newArray)