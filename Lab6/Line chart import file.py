import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

data = pd.read_csv('Lab6\sales_data.csv')
print(data.info())
print(style.available)

profist = data['total_profit'].tolist()
month = data['month_number'].tolist()
unit = data['total_units'].tolist()

plt.style.use("Solarize_Light2")
plt.figure('abcd')
plt.plot(month, profist,'-.')
plt.fill_between(month, unit, profist, color = 'red', alpha= 0.8)
plt.plot(month, unit)

plt.xlabel("Thang")
plt.ylabel('Loi nhuan')
plt.xticks(month)
plt.title('Line chart')
plt.yticks([100000,200000,300000,400000,500000])
plt.show()  
