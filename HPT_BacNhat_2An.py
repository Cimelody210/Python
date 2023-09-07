a1 = int(input("Nhập số a1: "))
b1 = int(input("Nhập số b1: "))
c1 = int(input("Nhập số c1: "))
a2 = int(input("Nhập số a2: "))
b2 = int(input("Nhập số b2: "))
c2 = int(input("Nhập số c2: "))
D = a1*b2-a2*b1
Dx= c1*b2-c2*b1
Dy = a1*c2- a2*c1
if D==0:
    if Dx+Dy ==0:
        print("Vo so nghiem")
    else:
        print("Vo nghiem")
else:
    x = Dx/D
    y = Dy/D
    print(f"Hệ phương trình có nghiệm là \n x = {x}\n y = {y}")
