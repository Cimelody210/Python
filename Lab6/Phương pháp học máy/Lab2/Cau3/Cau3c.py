from sklearn.preprocessing import normalize
import numpy as np

array = [[ 1., -1.,  2.],
     [ 2.,  0.,  0.],
     [ 0.,  1., -1.]]

X_normalized = normalize(array, norm='l2')
print("\nPhương pháp chuẩn hóa với chuẩn L2 ")
print(X_normalized)

# kq = sqrt(+++)
# item[i] / kq

# 0.408, -0.408,  0.816
# 1     0     0
# 0     0.707, -0.707