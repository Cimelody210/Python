from Ps import PhanSo
def Main():
    print("\n0.Thoát chương trình")
    print("\n1.Thực hiện phép cộng 2 phân số")
    print("\n2.Thực hiện phép trừ 2 phân số")
    print("\n3.Thực hiện phép nhân 2 phân số")
    print("\n4.Thực hiện phép chia 2 phân số")
    while True:
        luachon = int(input("Nhập lựa chọn ở đây: "))
       
        if luachon==0:
            print('Exit')
            break
        elif luachon ==1:
            print("Cộng 2 phân số")
            a=PhanSo()
            b=PhanSo()
            a.mau=int(input("Nhập mẫu của phân sô 1(khác 0): "))
            if a.mau != 0:
                a.tu=int(input("Nhập tử của phân sô 1(khác 0): "))
            else:
                print("Nhap sai, thoat chuong trinh")
                exit()
            if b.mau != 0:
                b.tu=int(input("Nhập tử của phân sô 2: "))
                print("Kết quả khi cộng 2 phân số là: {0} + {1} = {2}".format(a,b,a.__add__(b)))
            else:
                print("Nhap sai, thoat chuong trinh")
                exit()
        elif luachon == 2:
            print("Cộng 2 phân số")
            a=PhanSo()
            b=PhanSo()
            a.mau=int(input("Nhập mẫu của phân sô 1(khác 0): "))
            if a.mau != 0:
                a.tu=int(input("Nhập mẫu của phân sô 1(khác 0): "))
            else:
                print("Nhap sai, thoat chuong trinh")
                exit()
            if b.mau != 0:
                b.tu=int(input("Nhập tử của phân sô 2: "))
                b.mau=int(input("Nhập mẫu của phân sô 2: "))
                print("Kết quả khi cộng 2 phân số là: {} - {} = {}".format(a,b,a.__sub__(b)))
            else:
                print("Nhap sai, thoat chuong trinh")
                exit()
            
        elif luachon == 3:
            print("Nhân 2 phân số")
            a=PhanSo()
            b=PhanSo()
            a.mau=int(input("Nhập mẫu của phân sô 1(khác 0): "))
            if a.mau != 0:
                a.tu=int(input("Nhập mẫu của phân sô 1(khác 0): "))
            else:
                print("Nhap sai, thoat chuong trinh")
                exit()
            if b.mau != 0:
                b.tu=int(input("Nhập tử của phân sô 2: "))
                print("Kết quả khi cộng 2 phân số là: {} * {} = {}".format(a,b,a.__mul__(b)))
            else:
                print("Nhap sai, thoat chuong trinh")
                exit()
            
        elif luachon == 4:
            print("Cộng 2 phân số")
            a=PhanSo()
            b=PhanSo()
            a.mau=int(input("Nhập mẫu của phân sô 1(khác 0): "))
            if a.mau != 0:
                a.tu=int(input("Nhập mẫu của phân sô 1(khác 0): "))
            else:
                print("Nhap sai, thoat chuong trinh")
                exit()
            if b.mau != 0:
                b.tu=int(input("Nhập tử của phân sô 2: "))
                print("Kết quả khi cộng 2 phân số là: {} / {} = {}".format(a,b,a.__truediv__(b)))
            else:
                print("Nhap sai, thoat chuong trinh")
                exit()
            break
Main()