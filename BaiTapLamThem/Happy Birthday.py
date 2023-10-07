# Dành cho mấy khứa ế trong đó có cả tau :)
from random import *
import time

for i in range(1, 100):
    print(' ')
p = ' '
for i in range(1, 100):
    cv = randint(1, 100)
    while cv > 0:
        p += " "
        cv -= 1
    if i % 10 ==0:
        print(p+'Không có ny à =))')
        print(p+'Không sao :))')
    elif i % 8 ==0:
        print(p +'Kệ cha chúng nó😗')
    elif i % 6 ==0:
        print(p +'😚')
    elif i % 4 ==0:
        print(p +'😂')
    elif i % 2 ==0:
        print(p+'Happy Birthday!  💀🤡')
    else:
        print(p +'❤')
    p  = " "
    time.sleep(0.5)
        