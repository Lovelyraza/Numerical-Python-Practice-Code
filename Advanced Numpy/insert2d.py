import numpy as np
arr=np.array([[10,20,30],
              [40,50,60],
              [80,70,80]])
print(arr)
new_array=np.insert(arr,1,[11,22,33],axis=1)
print(new_array)
new_array=np.insert(arr,1,[11,22,33],axis=0)
print(new_array)
new_array=np.insert(arr,1,[11,22,33],axis=None)
print(new_array)

