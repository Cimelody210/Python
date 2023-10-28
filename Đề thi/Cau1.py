import datetime
class KhachHang:
    def __init__(self, hoTen:str, ngaysinh:datetime,sdt:str, diemtichluy:int) -> None:
        self.hoten = hoTen
        self.ngaysinh = ngaysinh
        self.sdt = sdt
        self.diemTL = diemtichluy
    def __str__(self) -> str:
        return f'{self.hoten}\t{self.ngaysinh}\t{self.sdt}\t{self.diemTL}'
    
    @classmethod
    def is_valid_Phone(self, sdt:str):
        return len(sdt) == 10
class DSKH:
    def __init__(self) -> None:
        self.dskh =[]
    def ThemKH(self, kh:KhachHang):
        self.dskh.append(kh)
    def xuat(self):
        for kh in self.dskh:
            print(kh)