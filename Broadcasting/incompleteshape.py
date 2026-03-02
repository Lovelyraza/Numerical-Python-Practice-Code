import numpy as np
arr=np.array([1,2,3,4])
ar=arr.reshape(2,2)
arr2=np.array([9,3,4,2])
arrrr=arr2.reshape(2,2)
ar=ar+arr2
print(ar)