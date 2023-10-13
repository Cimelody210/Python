import datetime
class SinhVien:
    def __init__(self, maSo:int, hoTen:str, ngaySinh:datetime, diemRL:int):
        self.maSo =maSo
        self.hoTen = hoTen
        self.ngaySinh =ngaySinh
        self.diemRL = diemRL 
    def __str__(self) -> str:
        return f'{self.maSo} \t {self.hoTen} \t {self.ngaySinh} \t {self.diemRL}'
