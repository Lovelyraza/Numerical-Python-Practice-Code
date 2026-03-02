import numpy as np

# arr=np.array([1,2,3,np.nan,4,5,6,-np.nan,6])
arr=np.array([1,2,3,np.inf,4,5,6,-np.inf,6])
# # print(np.isnan(arr))
# print(np.isinf(arr))

# # proper_value=np.nan_to_num(arr,posinf=10,neginf=40)
# # print(proper_value)
print(np.isinf(arr))
new_arr=np.nan_to_num(arr,posinf=34,neginf=45 )
print(new_arr)