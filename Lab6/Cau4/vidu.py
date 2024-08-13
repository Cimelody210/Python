import numpy as np
from statistics import *
from fractions import Fraction

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# print(len(speed))
# Tính giá trị trung bình của các phần tử trong mảng
print(np.mean(speed))
# Tính giá trị ở giữa
print(np.median(speed))

print(stdev(speed))
print(variance(speed))
print("Percentiles: "+ str(np.percentile(speed, 90)))