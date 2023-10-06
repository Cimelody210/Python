
from math import *
def PTB3():
    a =0
    try:
        while a==0:
            a= int(input("nhap he so a: "))
        b= int(input("nhap he so b: "))
        c= int(input("nhap he so c: "))
        d= int(input("nhap he so d: "))
    except:
        print('Dau vao sai: ')
    if a+b+c+d==0:
        delta = (a+b)**2 - 4*a*(a+b+c)
        if delta < 0:
            print("Nhan 1 nghiem: x = 1")
        elif delta ==0:
            Q = -(a+b)/(2*a)
            print("Nhan 2 nghiem: x1 = 1 va x2 = {}".format(Q))
        else:
            W1= int((-(a+b) + sqrt(delta))/(2*a))
            W2= int((-(a+b) - sqrt(delta))/(2*a))
            print("Nhan 3 nghiem:\nx1 = 1 \nx2 = {}\nx3 = {}".format(W1,W2))
    elif a-b+c-d ==0:
        delta = (b-a)**2 - 4*a*(c-b+a)
        if delta < 0:
            print("Nhan 1 nghiem: x = 1")
        elif delta ==0:
            E = int(-(b-a)/(2*a))
            print("Nhan 2 nghiem: x1 = 1 va x2 = {}".format(E))
        else:
            E1= int((-(b - a) + sqrt(delta))/(2*a))
            E2= int((-(b - a) - sqrt(delta))/(2*a))
            print("Nhan 3 nghiem:\nx1 = 1 \nx2 = {}\nx3 = {}".format(E1,E2))
    else:
        delta = b*2 - 3*a*c
        if delta ==0:
            T=  (-b +(b**3 - 27*(a**2)*d)**(1/3))/(3*a)
            print(f"Nhan 1 nghiem la x = {T}")
        else:
            k = (9*a*b*c - 2*b**3 - 27*(a**2*d))/(2*sqrt(abs(delta))**3)
            if delta < 0:
                Y = int(sqrt(abs(delta))/(3*a) * ((k + sqrt(k**2 + 1))**(1/3) + (k - sqrt(k**2 + 1))**(1/3))*b/(3*a))
                print(f"Nhan 1 nghiem la x = {Y}")
            elif delta >0 and abs(k) <= 1:
                F1 = int((2*sqrt(delta)*acos(cos(k)/3) - b)/(3*a))
                F2 = int((2*sqrt(delta)*acos(cos(k)/3) - (2*pi)/3 - b)/(3*a))
                F3 = int((2*sqrt(delta)*acos(cos(k)/3) + (2*pi)/3 - b)/(3*a))
                print(f"Nhan 3 nghiem la:\nx1 = {F1} \nx2 = {F2} \nx3 = {F3}")
            elif delta >0 and abs(k) > 1:
                F4 = int((sqrt(delta) * abs(k))/(3*a*k) * ((abs(k)+sqrt(k**2-1))**(1/3)+ (abs(k) - sqrt(k**2-1))**(1/3)) * b/(3*a))
                print(f"Nhan 1 nghiem la x = {F4}")
PTB3()
 
