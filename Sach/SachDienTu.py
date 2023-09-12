from Sach import Sach
class SachDienTu(Sach):
    def __init__(self, tensach: str, tentacgia: str, ngayxuatban: str, sotrang: int, giabia: int, dungluong:int) -> None:
        super().__init__(tensach, tentacgia, ngayxuatban, sotrang, giabia)
        self.dungluong = dungluong
    def TinhGiaBan_DienTu(self):
        if self.dungluong >10:
            price = self.giabia - self.giabia/4 + 10000
        else:
            price = self.giabia - self.giabia/4
        return price