


import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import numpy as np

x = [5,7,8,7,2,17,2,9,4,11,12,9,6]
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mymodel = np.poly1d(np.polyfit(x, y, 3))
myline = np.linspace(2, 95, 100)
speed = mymodel(10.5)

# Predict Future Values
# print(r2_score(y, mymodel(x)))
# print(speed)
# 0.8816766587791962
# 80.4799412981771

plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.show()




