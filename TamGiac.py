from math import *
def Triangle():
    a = float(input('Nhập số cạnh thứ 1: '))
    b = float(input('Nhập số cạnh thứ 2: '))
    c = float(input('Nhập số cạnh thứ 3: '))
    if a+b>c and b+c>a and c+a>b:
        if a==b==c:
            print("\nTam giac deu")
        if pow(a,2)+pow(b,2) == pow(c,2) or pow(b,2)+pow(c,2) == pow(a,2) or pow(a,2)+pow(c,2) == pow(b,2):
            print("\nTam giac vuong")
        else:
            print("\nTam giac thuong")
        p =(a+b+c)/2
        cosA = (pow(a,2)+pow(b,2)-pow(c,2))/(2*a*b)
        cosB = (pow(b,2)+pow(c,2)-pow(a,2))/(2*b*c)
        cosC = (pow(a,2)+pow(c,2)-pow(b,2))/(2*a*c)
        S = sqrt(p*(p-a)*(p-b)*(p-c))
        R = (a*b*c)/(4*S)
        r = S/p
        V_tudien = (a*b*c*sqrt(1 + 2*cosA*cosB*cosC - pow(cosA,2) - pow(cosB, 2) - pow(cosC,2)))/6
        print('\nGiá trị góc A là: {:.0f} độ' .format(180*(acos(cosA)/pi)))
        print('Giá trị góc B là: {:.0f} độ' .format(180*(acos(cosB)/pi)))
        print('Giá trị góc C là: {:.0f} độ' .format(180*(acos(cosC)/pi)))
        print("\nĐường cao của tam giác là: {:.1f}".format(2*S/a))
        print("\nBán kính đường tròn ngoại tiếp tam giác là: {:.1f}".format(R))
        print("\nBán kính đường tròn noi tiếp tam giác là: {:.1f}".format(r))
        print("\nDiện tích tam giác là: {:.1f} ".format(S))
        print("\nThể tích khối tứ diện S.ABC khi đã biết các góc trong đỉnh: {:.1f} ".format(V_tudien))
    else:
        print('Khong co tam giac nao dc toa thanh')
Triangle()