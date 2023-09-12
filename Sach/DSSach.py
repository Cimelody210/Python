from Sach import Sach
class DSSach:
    def __init__(self, ds=[]) -> None:
        self.ds = list(ds)

    def Them(self, sach: Sach):
        self.ds.append(sach)
    
    
    def TimTheoNam(self, nam:int):
        kq = DSSach()
        for sach in self.ds:
            if sach.ngayxuatban == nam:
                kq.ds.append(sach)
            return kq
    def TimTheoTacGia(self, ten_tacgia:str):
        return DSSach([sach for sach in self.ds if sach.tentacgia.lower().__contains__(ten_tacgia.lower())])
    
        # kq = DSSach()
        # for sach in self.ds:
        #     if sach.tentacgia ==ten:
        #         kq.ds.append(sach)
        #     return kq
    def TimTheoSoTrang(self, so_trang):
        kq = DSSach()
        for sach in self.ds:
            if sach.sotrang > so_trang:
                kq.ds.append(sach)
            return kq
    # def Xuat(self, dsSach):
    #     print("\t\t{:<8} {:<18} {:<8}".format("Tên sách", "Tên tác giả", "Ngày xuất bản",'Số trang','Giá bán'))
    #     for sach in dsSach:
    #         print("\t\t{:<8} {:<18} {:<8}".format(sach.tensach, sach.tentacgia, sach.ngayxuatban, sach.sotrang, sach.giabia))

    # def SapXepTheoTG(self):
    #     self.ds.sort(lambda x: x.ten)
    
    # def SapXepTheoNamxb(self):
    #     self.ds.sort(lambda x:(x.nam, x.ten))

