import numpy as np
import pandas as pd


arr1 = np.array([1, 2, 3,-1,5], dtype=int) 
arr2 = np.array([4, 5, 6,0,-2]) 
result = np.multiply(arr1, arr2) 
kq_add = np.add(arr1, arr2) 
kq_chia = np.divide(arr1, arr2) 
kq_tru = np.subtract(arr1, arr2) 
print(result)
print(kq_add)
print(kq_tru)
print(kq_chia)  