import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

data = pd.read_csv('Lab6\sales_data.csv')
print(data.info())
print(style.available)


profist = data['total_profit'].tolist()
month = data['month_number'].tolist()

plt.style.use("Solarize_Light2")
# plt.scatter(month, profist, edgecolors='green', linestyle='-')
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)

plt.figure('abcd')
plt.plot(month, profist)
plt.xlabel("Thang")
plt.ylabel('Loi nhuan')
plt.xticks(month)
plt.title('Line chart')
plt.yticks([100000,200000,300000,400000,500000])
plt.show()  