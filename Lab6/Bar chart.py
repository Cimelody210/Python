import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([22,17,7,10.8, 5.8, 8, 35.8])

plt.bar(x, y, color = "red", width=0.8)
# plt.barh(x, y)

plt.show()