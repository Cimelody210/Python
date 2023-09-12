from datetime import datetime
from tabulate import tabulate
from DSSVChinhQuy import DSSinhVien
from DSSVPhiChinhQuy import DSSVPhiChinhQuy
from DanhSach import DanhSach

def Main():
    print('''
        0. Thoát chương trình
        1. In danh sách sinh viên
        2. Đọc và in file danh sách
        3. Tìm sinh viên theo mã số
        4. Tìm sinh viên theo trình độ
        5. Tìm sinh viên có điểm rèn luyện trên 80
        6. Danh sách sinh viên cao đẳng sinh trước ngày 15/08/1999
    ''')
    while True:
        luachon = int(input("Nhập lựa chọn của bạn: "))
        if luachon == 0:
            print("Exit")
            break
        elif luachon == 1:
            sv1 = DSSinhVien(2011423,"Ngô Hoài Phong",datetime.strptime("01/1/2002","%d/%m/%Y"),84)
            sv2 = DSSinhVien(2012378,"Đặng Ngọc Thắng",datetime.strptime("6/12/2000","%d/%m/%Y"),80)
            sv7 = DSSinhVien(2114789,"Lưu Văn Quyết",datetime.strptime("16/7/2003","%d/%m/%Y"),85)

            sv3 = DSSinhVien(2012395,"Nguyễn Hữu Trọng",datetime.strptime("6/2/2002","%d/%m/%Y"),90)
            sv4 = DSSinhVien(2011432,"Nguyễn Tuấn Kiệt",datetime.strptime("20/11/2002","%d/%m/%Y"),79)
            sv5 = DSSinhVien(2011432,"Nguyễn Tuấn Kiệt",datetime.strptime("20/11/2002","%d/%m/%Y"),79)
            sv6 = DSSinhVien(2114789,"Hoàng Minh Chiến",datetime.strptime("20/4/2003","%d/%m/%Y"),75)
            sv14 = DSSinhVien(2114789,"Yu Xiaoming",datetime.strptime("20/4/2003","%d/%m/%Y"),60)
            sv15 = DSSinhVien(2114789,"Hoàng Minh Chiến",datetime.strptime("20/4/2003","%d/%m/%Y"),50)
            sv12 = DSSinhVien(2110236,"Lý Cây Chanh",datetime.strptime("10/12/2003","%d/%m/%Y"),67)

            sv8 = DSSVPhiChinhQuy(2011212,"Nguyễn Văn A",datetime.strptime("1/1/2002","%d/%m/%Y"),"Cao Đẳng",2)
            sv9 = DSSVPhiChinhQuy(1934823,"Giulitano Tell",datetime.strptime("7/2/2001","%d/%m/%Y"),"Cử nhân",5)
            sv10 = DSSVPhiChinhQuy(1647852,"Trần Khánh Vy",datetime.strptime("21/8/1999","%d/%m/%Y"),"Cử nhân",5)
            sv11 = DSSVPhiChinhQuy(2110526,"Lê Tiến Linh",datetime.strptime("26/8/2000","%d/%m/%Y"),"Tiến sĩ",4)
            
            sv13 = DSSinhVien(2114569,"Hoàng Bảo Trinh",datetime.strptime("1/10/2003","%d/%m/%Y"),90)
            
            dssv=DanhSach()
            dssv.ThemSinhVien(sv1)
            dssv.ThemSinhVien(sv13)
            dssv.ThemSinhVien(sv14)
            dssv.ThemSinhVien(sv15)
            dssv.ThemSinhVien(sv12)
            dssv.ThemSinhVien(sv7)
            dssv.ThemSinhVien(sv2)

            dssv.ThemSinhVien(sv8)
            dssv.ThemSinhVien(sv9)
            dssv.ThemSinhVien(sv10)
            dssv.ThemSinhVien(sv11)

            dssv.ThemSinhVien(sv3)
            dssv.ThemSinhVien(sv4)
            dssv.ThemSinhVien(sv5)
            dssv.ThemSinhVien(sv6)

            print(tabulate(['','','','','',''],headers=['MSSV','Họ và tên','Ngày sinh','Điểm rèn luyện','Hệ đào tạo','Thời gian đào tạo']))
            dssv.Xuat()
        elif luachon == 2:
            print("\nChưa nghĩ ra cách nào khả quan hơn: ")
            print("Distinguished student: Học sinh ưu tú")
        elif luachon == 3:
            dssv.Xuat()
            mssv = int(input("\nNhập MSSV cần tìm: "))
            vt = dssv.timSVTheoMS(mssv)
            print(f"Sinh viên ở vị trí thứ {vt+1} trong danh sách") if vt>0 else print(f'Không tồn tại sinh viên có mã số {mssv} trong danh sách')
        elif luachon == 4:
            dssv.Xuat()
            trinh_do =str(input("\nNhập trình độ đào tạo: "))
            kq=dssv.TimSinhVienTheoLoai(trinh_do)
            print("Danh sách sinh viên theo loại {}".format(trinh_do))
            for sv in kq:
                print(sv)
        elif luachon == 5:
            print('\n')
            dssv.Xuat()
            # diemRL = int(input("Nhập điểm rèn luyện: "))
            kq = dssv.TimSinhVienCoDRLTu80TroLen(80)
            print("\nDanh sách sinh viên có điểm rèn luyện lớn hơn 80 là")
            for sv in kq:
                print(sv)
        elif luachon == 6:
            kq = dssv.TimSinhVienSinhTruocNgay("15/4/2003",'%d%m%Y')
            print("\nDanh sách sinh viên sinh trước ngày 15/8/1999")
            for sv in kq:
                print(sv)
        else:
            print('Sai: Nhap lai lua chon: ')
            break


Main()