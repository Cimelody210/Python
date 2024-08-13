# Vẽ đồ thị hàm số bất kỳ và tìm xem phương trình f(x) = g(x) có bao nhiêu nghiệm
import matplotlib.pyplot as plt
import numpy as np
from math import *

#  Nhập đồ thị f và g ở đây
def f(x):
    return (2*x**4 - x**2 +1)/(x**2 - 9)
def g(x1):
    return 3*x1**2 - 2*x1
     
def Main():
     abc =  np.linspace(-10,20,40)
     y = f(abc) 
     y1 = g(abc)
     plt.plot(abc,y)
     plt.plot(abc,y1)
     plt.xlim(-10,10)
     plt.ylim(0,600)
     plt.show()

Main()