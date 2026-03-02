import numpy as np

arr=np.array([1,2,3,np.nan,4,5,6,np.nan,6])
print(np.isnan(arr))

proper_value=np.nan_to_num(arr,nan=10)
print(proper_value)