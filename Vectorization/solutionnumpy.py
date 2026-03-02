import numpy as np
prices=np.array([100,200,300,400,500,600,700])
dicount=10
dicount_arr=prices-(prices*dicount/100)
print(dicount_arr)