#numpy it is works like array

import numpy as np

x=np.array([1,2,3,4,5])
y=np.array([34,56])
print(x.shape)
print(y.shape)
print(np.concatenate((x,y)))

slice = x[1:3:2]
print(slice)
arr = np.array([
    [1,2],[3,4],
    [5,6],[7,8],
    [9,10],[11,12],
    [13,14],[15,16],
])
z = np.array_split(arr,3)
print(z)