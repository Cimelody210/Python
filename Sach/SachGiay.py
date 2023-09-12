from Sach import Sach
class SachGiay(Sach):
    def __init__(self, tensach:str, tentacgia:str, ngayxuatban:str, sotrang:int, giabia:int, trongluong:int) -> None:
        super().__init__(tensach,tentacgia, ngayxuatban,sotrang,giabia)
        self.trong_luong = trongluong
    def TinhGiaBan_Giay(self):
        return self.giabia - 0.05 * self.giabia+ self.trong_luong * 100