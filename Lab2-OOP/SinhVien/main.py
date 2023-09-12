from QLSV import QLSV
from tabulate import tabulate
qlsv = QLSV()
def Main():
    while (1==1):
        print('\n0 Thoat chuong trinh: ')
        print('1/ Xuất danh sách từ file text')
        print('2/ Add Junior')
        print('3/ Hien thi danh sach sinh vien')
        print('4/ Cap nhat sinh vien')
        print('5/ Tim sinh vien theo ten')
        print('6/ Sap xep sinh vien tang theo ten')
        luachon =int(input("Nhập lựa chọn ở đây: "))
        if luachon ==0:
            print('\nExit')
            break
        elif luachon ==1:
            print(tabulate(['','','',''],['STT','MSSV', 'Họ và tên','Ngày sinh','Điểm rèn luyện']))
            qlsv.DocFile()
        elif luachon ==2:
            qlsv.NhapSV()
            print("Success")
        elif luachon ==3:
            if qlsv.DocFile() > 0:
                qlsv.show(qlsv.GetListSV())
            else:
                print('\nDanh sách trống')
        elif luachon ==4:
            if qlsv.SoLuongSV() > 0:
                mssv =int(input('Nhập MSSV:'))
                qlsv.Update(mssv)
            else:
                print('\nDanh sách trống')
        elif luachon ==5:
            if qlsv.SoLuongSV() > 0:
                name =str(input('Nhập tên cần tìm:'))
                kq= qlsv.TimSV_TheoTen(name)
                qlsv.show(kq)
            else:
                print('\nDanh sách trống')
        elif luachon ==6:
            if qlsv.SoLuongSV() > 0:
                qlsv.TangTheoTen()
                qlsv.show(qlsv.GetListSV())
            else:
                print('\nDanh sách trống')
    else:
        print("Khong co chuc nang nay")
Main()