# Áp dụng vào trong bài Writing Task 1

import numpy as np 
import matplotlib.pyplot as plt 
barWidth = 0.1
# set height of bar

# Các cột dữ liệu
Chelsea = [50, 40, 45, 43]
MU = [12,24,27,87]
ED = [12,45,34, 17]
dd  =[34,63,42,63]

# Tháng
thang =['1','2','3','4']

# Set position of bar on X axis
br1 = np.arange(len(Chelsea))
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3] 

# Make the plot
plt.bar(br1, Chelsea, color ='blue', width = barWidth,  edgecolor ='blue', label ='Chelsea') 
plt.bar(br2, MU, color ='red', width = barWidth, edgecolor ='red', label ='MU') 
plt.bar(br3, ED, color ='cyan', width = barWidth, edgecolor ='cyan', label ='ed') 
plt.bar(br4, dd, color ='yellow', width = barWidth, edgecolor ='gray', label ='ed') 

plt.title('The chart below shows the changes in three different areas \n of crime in Manchester city centre from 2003-2012', font='12px')
plt.xlabel('Branch', fontweight ='bold')
plt.ylabel('Students passed', fontweight ='bold') 
plt.xticks([r + barWidth for r in range(len(Chelsea))],thang)
plt.yticks([10,20,30,40,50,60,70,80,90,100])
# Chú thích các cột
plt.legend(['Chelsea','Manchester United','West Harm','Liverpool'])
plt.show() 
