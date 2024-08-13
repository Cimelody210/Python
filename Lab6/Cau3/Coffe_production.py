# Áp dụng vào trong bài Writing Task 1

import numpy as np 
import matplotlib.pyplot as plt 
barWidth = 0.1
# set height of bar

# Các cột dữ liệu
Bra = [30, 50, 64, 76]
cot2 = [20, 11, 9, 9.5]
cot3 = [12,20,18, 17]
cot4  =[9,6.3,24,36]

# Tiêu đề cho các nước
thang =['1990','1995','2000','2010']

# Set position of bar on X axis
br1 = np.arange(len(Bra))
br2 = [x + barWidth for x in br1] 
br3 = [x + barWidth for x in br2]
br4 = [x + barWidth for x in br3] 

# Make the plot
plt.bar(br1, Bra, color ='blue', width = barWidth,  edgecolor ='blue', label ='Chelsea') 
plt.bar(br2, cot2, color ='red', width = barWidth, edgecolor ='red', label ='MU') 
plt.bar(br3, cot3, color ='cyan', width = barWidth, edgecolor ='cyan', label ='ed') 
plt.bar(br4, cot4, color ='yellow', width = barWidth, edgecolor ='gray', label ='ed') 

plt.title('The graph gives information about coffee production \n in 4 different countries from 1990 to 2010')
plt.xlabel('', fontweight ='bold')
plt.ylabel('Million tonnes', fontweight ='bold') 
plt.xticks([r + barWidth for r in range(len(Bra))], thang)
plt.yticks([10,20,30,40,50,60,70,80,90,100])

# Chú thích các cột
plt.legend(['Brazil','Argentina','Colombia','Venezuala'], ncol = 4)
plt.show() 
