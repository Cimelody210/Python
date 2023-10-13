from datetime import datetime
from tabulate import tabulate
from DSSVChinhQuy import DSSinhVien
from DSSVPhiChinhQuy import DSSVPhiChinhQuy
from SInhVien import SinhVien
class DanhSach:
    def __init__(self) -> None:
        self.dssv=[]
    
    def ThemSinhVien(self,sv:SinhVien):
        self.dssv.append(sv)
    
    def Xuat(self):
        if self.dssv.__len__() > 0:
            for sv in self.dssv:
                print(sv)
                # print('{:<10}'.format(sv))
            
    def timSVTheoMS(self,ms:int):
        for svi in range(len(self.dssv)):
            if self.dssv[svi].MaSo==ms:
                return svi
        else:
            return -1

    def TimSinhVienTheoLoai(self,loai:str):
        if loai =='chinhquy':
            return [sv for sv in self.dssv if isinstance(sv,DSSinhVien)]
        return [sv for sv in self.dssv if isinstance(sv,DSSVPhiChinhQuy)]
    @staticmethod
    def KiemTraSV_DRL80(sv:SinhVien):
        if not isinstance(sv, DSSinhVien):
            return False
        if sv.diemRL >= 80:
            return True
        return False

    # Tìm sinh viên có điểm rèn luyện từ 80 trở lên
    def TimSinhVienCoDRLTu80TroLen(self,drl:int):
        return [sv for sv in self.dssv if self.KiemTraSV_DRL80(sv)]
    # #Tìm sinh viên có trình độ cao đẳng sinh trước 15/08/1999

    @staticmethod
    def KiemTraSV_CoNgaySinhTruoc(sv:SinhVien):
        if not isinstance(sv, DSSVPhiChinhQuy):
            return False
        if sv.trinhdo.lower()=='Cử nhân'.lower() and sv._ngaySinh < datetime.strptime('15/4/2003','%d%m%Y'):
            return True
        return False
    def TimSinhVienSinhTruocNgay(self,ngaySinh:datetime):
        return [sv for sv in self.dssv if self.KiemTraSV_CoNgaySinhTruoc(sv)]